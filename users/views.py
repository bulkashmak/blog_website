from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from posts.models import Post
from .forms import EditProfileForm


def register(request):
    """
    View to register new users on the website.
    """
    template = 'registration/register.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home_page')
    else:
        form = UserCreationForm()

    context = {
        'title': 'Registration',
        'form': form,
    }

    return render(request, template, context)


@login_required
def account_details(request):
    posts = Post.objects.filter(author=request.user)

    context = {
        'title': 'Account',
        'posts': posts.order_by('-created'),
    }

    return render(request, 'users/account.html', context)


@login_required
def edit_profile(request):
    """
    Edit profile info: username, First name, Last name, email
    """
    template = 'users/edit_profile.html'

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account_details')
    else:
        form = EditProfileForm()

    context = {
        'title': 'Edit Profile',
        'form': form
    }

    return render(request, template, context)
