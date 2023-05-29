from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['education_format', 'lecture_class', 'labaratory_class', 'year_enrollment', 'course_name', 'instructors', 'prerequisites', 'description', 'learning_outcomes']