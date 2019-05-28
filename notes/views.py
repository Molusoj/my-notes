from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def home(request):
    if User.is_authenticated:
        return render(request, 'notes/home.html')
    else:
        redirect('cover')


def cover(request):
    return render(request, 'notes/cover.html')
