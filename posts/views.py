from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CreatePost


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
def create_post_page(request):

    if request.method == "POST":
        # author = Post(author=request.user)
        form = CreatePost(request.POST)

        if form.is_valid():
            f_title = form.cleaned_data["title"]
            f_content = form.cleaned_data["content"]
            f_status = form.cleaned_data["status"]
            new_post = Post(title=f_title,
                            content=f_content,
                            status=f_status,
                            author=request.user)
            new_post.save()

            return redirect('posts_page')
    else:
        form = CreatePost()

    context = {
        'title': 'New Post',
        'form': form,
    }

    return render(request, 'posts/create_post.html', context)
