import time
from urllib import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

from club.views import newmeeting
from .models import Meeting, Resource, MeetingMinutes, Event
import datetime
from .forms import MeetingForm, ResourceForm

# Create your tests here.
class MeetingTest (TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='Test Meeting 1.1')
        self.meeting=Meeting(
            meetingtitle=self.title,
            meetingdate='2022-03-30',
            meetingtime='15:30:00',
            meetinglocation='Off-campus',
            meetingagenda='See previous team email'
            )

    def test_meetingstring(self):
        self.assertEqual(str(self.type),'Test Meeting 1.1')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest (TestCase):
    def setUp(self):
        self.type=Resource(resourcetype='Example Resource')
        self.name=Resource(resourcename='Website')
        self.resource=Resource(
            resourcename=self.name,
            resourcetype=self.type,
            resourceurl='sampleurl.test.com',
            entrydate='2022-03-25',
            description='Testing Description'
            )
    
    def test_resourcestring(self):
        self.assertEqual(str(self.type),'Example Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table),'resource')

class MeetingMinutesTest (TestCase):
    def setUp(self):
        self.type=MeetingMinutes(minutestext='Sample Minutes Text')
    
    def test_minutesstring(self):
        self.assertEqual(str(self.type),'Sample Minutes Text')
    
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table),'meetingminutes')

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data={
            'meetingtitle' : "Test Meeting",
            'meetingdate' : '2022-04-01', 
            'meetingtime' : "12:00:00", 
            'meetinglocation' : "Off-campus",
            'meetingagenda' : "See previous team email"
            }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)
    
    def test_meetingform_minus_meetingagenda(self):
        form=MeetingForm(data={'meetingtitle': "Test Meeting"})
        self.assertTrue(form.is_valid())

    def test_meetingform_empty(self):
        form=MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())

class NewResourceForm(TestCase):
    def test_resourceform(self):
        data={
            'resourcename' : "Example Resource",
            'resourcetype' : "Website", 
            'resourceurl' : "resource.url.io", 
            'entrydate' : "2022-03-26",
            'description' : "A description of the Resource will appear here"
            }
        form=ResourceForm(data)
        self.assertTrue(form.is_valid)
    
    def test_resourceform_minus_description(self):
        form=ResourceForm(data={'resourcename': "Example Resource"})
        self.assertTrue(form.is_valid())

    def test_resourceform_empty(self):
        form=ResourceForm(data={'resourcename': ""})
        self.assertFalse(form.is_valid())

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='Test Subject 4', password='P@ssw0rd1')
        self.title=Meeting.objects.create('Test Meeting 8')
        self.meeting=Meeting.objects.create(
            meetingtitle=self.title,
            meetingtime='12:00:00', 
            meetinglocation='Off-campus',
            meetingagenda='See previous team email'
            )
            
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, 'accounts/login/?next=/tech/newmeeting')