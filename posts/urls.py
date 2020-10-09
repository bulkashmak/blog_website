from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('posts/', views.posts_page, name='posts_page'),
    path('posts/create/', views.create_post_page, name='create_post_page'),
]
