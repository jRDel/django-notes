from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from .models import Note
from .forms import NoteForm


# Create your views here.

def show_notes(request):
    notes_list = Note.objects.all()
    
    template = loader.get_template('notesapp/all.html')
    context = {
        'notes_list': notes_list
    }
    return HttpResponse(template.render(context, request))

def show_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    print(str(note.description))
    template = loader.get_template('notesapp/note.html')
    context = {
        'note': note
    }
    return HttpResponse(template.render(context,request))

def new_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        note = Note()
        note.title = title
        note.description = description
        note.save()

    notes_list = Note.objects.all()

    template = loader.get_template('notesapp/all.html')
    context = {
        'notes_list': notes_list
    }
    return HttpResponse(template.render(context, request))
