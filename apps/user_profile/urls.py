from .views import *
from django.urls import path

urlpatterns = [ 
    # path('', home, name='welcome-page'),
    # path('signup/', user_signup, name='signup'),
    # path('login/', user_login,name='login'),
    # path('logout/', user_logout,name='logout'),
    path('change-password/', change_password, name='change-password'),
    path('', user_profile, name = 'profile'),
    path('edit_profile/', edit_user_profile, name = 'edit-profile'),


]