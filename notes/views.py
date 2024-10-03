from datetime import datetime

from django.db.models import F
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404, redirect

from .models import Note


def notes_view(request):
    # Annotate to use updated_at if available, otherwise use created_at
    notes = Note.objects.annotate(
        effective_date=Coalesce('updated_at', F('created_at'))
    ).order_by('-effective_date')

    current_year = datetime.now().year
    return render(request, 'notes/index.html', {'notes': notes, 'current_year': current_year})


def note_detail_view(request, title):
    note = get_object_or_404(Note, title=title)
    query = request.GET.get('query', '')
    current_year = datetime.now().year
    return render(request, 'notes/detail.html', {'note': note, 'query': query, 'current_year': current_year})


def search_notes(request):
    query = request.GET.get('query', '')
    notes = Note.objects.filter(content__icontains=query)
    current_year = datetime.now().year
    return render(request, 'notes/note_list.html', {'notes': notes, 'current_year': current_year})


def delete_note(request, title):
    note = get_object_or_404(Note, title=title)
    if request.user.is_superuser:
        note.delete()
    return redirect('notes_view')