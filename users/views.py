from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from posts.models import Post


def register(request):
    """
    View to register new users on the website.
    """
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

    return render(request, 'registration/register.html', context)


def account_details(request):
    posts = Post.objects.filter(author=request.user)

    context = {
        'title': 'Account',
        'posts': posts.order_by('-created'),
    }

    return render(request, 'users/account.html', context)
