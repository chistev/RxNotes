from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes_view'),
    path('note/<str:title>/', views.note_detail_view, name='note_detail_view'),
    path('search/', views.search_notes, name='search_notes'),
    path('note/<str:title>/delete/', views.delete_note, name='delete_note'),
]
