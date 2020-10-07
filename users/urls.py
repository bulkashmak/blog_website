from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.account_details, name="account_details"),
    path('register', views.register, name="register"),
]
