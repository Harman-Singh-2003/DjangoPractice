from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path ("allNotes/", views.NotesView.as_view(), name="note")
]