from django.urls import path

from .views import *

urlpatterns = [
    path("create", create_document, name="document_create"),
    path("success", success_document, name="success_document")
]
