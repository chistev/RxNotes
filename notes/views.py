from django.shortcuts import render, get_object_or_404, redirect

from .models import Note


def notes_view(request):
    notes = Note.objects.all().order_by('-updated_at')
    return render(request, 'notes/index.html', {'notes': notes})


def note_detail_view(request, title):
    note = get_object_or_404(Note, title=title)
    query = request.GET.get('query', '')
    return render(request, 'notes/detail.html', {'note': note, 'query': query})


def search_notes(request):
    query = request.GET.get('query', '')
    notes = Note.objects.filter(content__icontains=query)
    return render(request, 'notes/note_list.html', {'notes': notes})


def delete_note(request, title):
    note = get_object_or_404(Note, title=title)
    if request.user.is_superuser:
        note.delete()
    return redirect('notes_view')