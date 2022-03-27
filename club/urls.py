from django.contrib import admin 
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('meetings/', views.meetings, name='meetings'),
   path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
   path('newmeeting/', views.newmeeting, name='newmeeting'),
   path('newresource/', views.newresource, name='newresource'),
   path('admin/', admin.site.urls),
   path('club/', include('club.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]