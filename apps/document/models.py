from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from apps.corecode.models import DocumentClass


class Instractor(models.Model):
    ACADEMIC_CHOICES = [
        ("Professor", "prof"),
        ("Labaratory Insructor", "LI"),
        ("Teacher Assistant", "TA"),
        ("Research Assistant", "RA"),
        ("Labaratory Assistant", "LA"),
        ("Intern", "Intern"),
    ]

    ACADEMIC_DEGREE = [
        ("Professor", "prof"),
        ("PhD", "doctor"),
        ("Masters", "masters"),
        ("Bachelor", "bachelor"),
    ]

    name = models.CharField(max_length=30)
    academic_level = models.CharField(max_length=20, choices=ACADEMIC_CHOICES, default="Professor")
    academic_degree = models.CharField(max_length=50, choices=ACADEMIC_DEGREE, default="Professor")

    def __str__(self):
        return self.name + " " + self.academic_level


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Outcomes(models.Model):
    name = models.CharField(max_length=500)

class Document(models.Model):
    FORMAT_CHOICES = [("дневной", "Дневной"), ("вечерний", "Вечерний")]
    LECTURE_CHOICES = [
        ("physical science", "Physical Science"),
        ("chemical science", "Chemical Science"),
        ("biological science", "Biological Science"),
        ("geological science", "Geological Science"),
        ("math", "Math"),
        ("computer science", "Computer Science"),
    ]

    LAB_CHOICES = [
        ("physical experiments", "Physical Experiments"),
        ("physics teaching", "Physics Teaching"),
        ("chemical experiments", "Chemical Experiments"),
        ("chemical teaching", "Chemical Teaching"),
        ("biological experiments", "Biological Experiments"),
        ("geological experiments", "Geological Experiments"),
        ("math", "Math"),
        ("math teaching", "Math Teaching"),
        ("computer science research", "Computer Science Research"),
        ("computer science practical experience", "Computer Science practical experience"),
    ]

    COURSE_CHOICES = [
                        ("Data mining and big data", "big data"),
                        ("Data science and Machine learning", "ML&AI"),
                        ("Sofware engineering", "SWE"),
                        ("Airospace and mechanical engineering", "AME"),
                        ("Chemical engineering", "Chem eng"),
                        ("Computer science research methods", "RM"),
    ]

    education_format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default="дневной")
    lecture_class = models.CharField(max_length=20, choices=LECTURE_CHOICES, default="physical science")
    labaratory_class = models.CharField(max_length=50, choices=LAB_CHOICES, default="physical experiments")
    year_enrollment = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2099)])
    course_name = models.CharField(max_length=20, unique=True)
    instructors = models.ForeignKey(Instractor, on_delete=models.RESTRICT)
    # instructor = models.CharField(max_length=50)
    prerec_for = models.ForeignKey(Course, related_name='course_prerec_for', on_delete=models.RESTRICT) # symmetrical=False, blank=True)
    prerequisites = models.ForeignKey(Course, related_name='course_prerequisites', on_delete=models.RESTRICT, blank=True, null=True)
    description = models.CharField(max_length=5000)
    learning_outcomes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.course_name