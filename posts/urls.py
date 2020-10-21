from django.urls import path
from . import views


# app_name = 'posts'

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('', views.posts_page, name='posts_page'),
    path('posts/create/', views.create_post_page, name='create_post_page'),
    path('posts/delete/<int:post_id>', views.delete_post, name='delete_post'),
]
