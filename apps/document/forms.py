from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    learning_outcomes = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    year_enrollment = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'between 1900-2099'}))

    class Meta:
        model = Document
        fields = ['education_format', 'lecture_class', 'labaratory_class', 'year_enrollment', 'course_name', 'instructors', 'prerequisites', 'prerec_for', 'description', 'learning_outcomes']
        labels = {
            'prerec_for' : 'Prerequisite for',
            'year_enrollment' : 'Year of enrollment',
        }

