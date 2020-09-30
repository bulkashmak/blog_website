from django.shortcuts import render
from .models import Post


def home_page(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'base.html', context)


def posts_page(request):
    posts = Post.objects.order_by('created')

    context = {
        'title': 'Posts',
        'posts': posts,
    }

    return render(request, 'posts/posts.html', context)


def about_page(request):

    context = {
        'title': 'About'
    }

    return render(request, 'posts/about.html', context)
