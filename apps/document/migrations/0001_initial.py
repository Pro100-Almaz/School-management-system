# Generated by Django 3.2.17 on 2023-05-29 16:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('academic_level', models.CharField(choices=[('Professor', 'prof'), ('Labaratory Insructor', 'LI'), ('Teacher Assistant', 'TA'), ('Research Assistant', 'RA'), ('Labaratory Assistant', 'LA'), ('Intern', 'Intern')], default='Professor', max_length=20)),
                ('academic_degree', models.CharField(choices=[('Professor', 'prof'), ('PhD', 'doctor'), ('Masters', 'masters'), ('Bachelor', 'bachelor')], default='Professor', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Outcomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_format', models.CharField(choices=[('дневной', 'Дневной'), ('вечерний', 'Вечерний')], default='дневной', max_length=20)),
                ('lecture_class', models.CharField(choices=[('physical science', 'Physical Science'), ('chemical science', 'Chemical Science'), ('biological science', 'Biological Science'), ('geological science', 'Geological Science'), ('math', 'Math'), ('computer science', 'Computer Science')], default='physical science', max_length=20)),
                ('labaratory_class', models.CharField(choices=[('physical experiments', 'Physical Experiments'), ('physics teaching', 'Physics Teaching'), ('chemical experiments', 'Chemical Experiments'), ('chemical teaching', 'Chemical Teaching'), ('biological experiments', 'Biological Experiments'), ('geological experiments', 'Geological Experiments'), ('math', 'Math'), ('math teaching', 'Math Teaching'), ('computer science research', 'Computer Science Research'), ('computer science practical experience', 'Computer Science practical experience')], default='physical experiments', max_length=50)),
                ('year_enrollment', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2099)])),
                ('description', models.CharField(max_length=5000)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.course')),
                ('instructors', models.ManyToManyField(to='document.Instractor')),
                ('learning_outcomes', models.ManyToManyField(to='document.Outcomes')),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='prerec_for', to='document.Course')),
            ],
        ),
    ]
