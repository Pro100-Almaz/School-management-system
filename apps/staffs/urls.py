from django.urls import path

from ..document.views import instructor_list, instructor_create

urlpatterns = [
    path("list/", instructor_list, name="instructor_list"),
    path("create", instructor_create, name='instructor_create')
]



# path("list/", StaffListView.as_view(), name="staff-list"),
#     path("<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
#     path("create/", StaffCreateView.as_view(), name="staff-create"),
#     path("<int:pk>/update/", StaffUpdateView.as_view(), name="staff-update"),
#     path("<int:pk>/delete/", StaffDeleteView.as_view(), name="staff-delete"),