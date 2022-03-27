from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from .models import Resource, Meeting, MeetingMinutes, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'