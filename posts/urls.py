from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('posts/', views.posts_page, name='posts_page'),
    path('new_post/', views.new_post_page, name='new_post_page'),
]
