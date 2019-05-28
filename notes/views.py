from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Note
from django.utils import timezone


def home(request):
    if User.is_authenticated:
        return render(request, 'notes/home.html')
    else:
        redirect('cover')


def cover(request):
    return render(request, 'notes/cover.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['note']:
            note = Note()
            note.title = request.POST['title']
            note.note = request.POST['note']
            note.manager = request.user
            note.save()
            return redirect('home')
        else:
            return render(request, 'notes/create.html', {'error': 'All Fields Required'})

    else:
        return render(request, 'notes/create.html')
