from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CreatePost
from .filters import PostFilter


def home_page(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'posts/home.html', context)


def posts_page(request):
    posts = Post.objects.order_by('-created')

    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    context = {
        'title': 'Posts',
        'posts': posts,
        'myFilter': myFilter,
    }

    return render(request, 'posts/posts.html', context)


def about_page(request):

    context = {
        'title': 'About'
    }

    return render(request, 'posts/about.html', context)


@login_required(login_url='registration/login.html')
def create_post_page(request):
    """
    Page for making new posts
    """

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


@login_required(login_url='registration/login.html')
def delete_post(request, post_id):
    """
    Deletes a post with id==post_id
    """
    post_obj = get_object_or_404(Post, id=post_id)
    post_obj.delete()
    return redirect('account_details')


@login_required(login_url='reqistration/login.html')
def edit_post(request, post_id):
    """
    Edit a post that has Draft status
    """
    template = 'posts/create_post.html'

    post_obj = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CreatePost(request.POST, instance=post_obj)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('account_details')
    else:
        form = CreatePost(instance=post_obj)

    context = {
        'form': form,
        'title': 'Edit Post'
    }

    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'

    post_obj = get_object_or_404(Post, id=post_id)

    context = {
        'post': post_obj,
        'title': post_obj.title,
    }

    return render(request, template, context)
