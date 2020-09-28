from django.shortcuts import render
# from .forms import LoginForm


def home_page(request):
    return render(request, 'base.html')
