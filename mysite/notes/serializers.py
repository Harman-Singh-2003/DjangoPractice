from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = (
            'title', 'content', 'last_updated', 'date_created'
        )