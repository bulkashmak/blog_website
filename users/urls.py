from django.urls import path, include
from . import views


# app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.account_details, name="account_details"),
    path('register', views.register, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
]
