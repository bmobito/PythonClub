from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('meetings/', views.meetings, name='meetings'),
   path('meetingDetails/<int:id>', views.meetingDetails, name='meetingDetails'),
]