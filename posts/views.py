from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


def home_page(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'posts/home.html', context)


def posts_page(request):
    posts = Post.objects.order_by('-created')

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


@login_required(login_url='registration/login.html')
def new_post_page(request):

    context = {
        'title': 'New Post',
    }

    return render(request, 'posts/new_post.html', context)
