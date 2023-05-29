from django.contrib import admin
from .models import AcademicSession, AcademicTerm

admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)