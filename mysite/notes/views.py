from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notes
from .serializers import NotesSerializer

# Create your views here.
def index(request):
    return HttpResponse("This is the notes app homepage")

class NotesView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
