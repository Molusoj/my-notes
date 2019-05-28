from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Note
from django.utils import timezone
from django.views.generic.edit import UpdateView, DeleteView


@login_required(login_url="/notes/cover")
def home(request):

    notes = Note.objects
    return render(request, 'notes/home.html', {'notes': notes})


def cover(request):
    return render(request, 'notes/cover.html')


@login_required(login_url="/notes/cover")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['note']:
            note = Note()
            note.title = request.POST['title']
            note.note = request.POST['note']
            note.manager = request.user
            note.save()
            return redirect('/notes/' + str(note.id))
        else:
            return render(request, 'notes/create.html', {'error': 'All Fields Required'})

    else:
        return render(request, 'notes/create.html')


@login_required(login_url="/notes/cover")
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/update.html'
    fields = ['title', 'note']
    success_url = '/'

    def form_valid(self, form):
    	instance = form.save()
    	return redirect('detail', instance.pk)

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    success_url = '/'