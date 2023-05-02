from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','parent','order']
#     list_filter = ('name',)

admin.site.register(CustomUser)