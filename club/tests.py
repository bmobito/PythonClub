import time
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Resource, MeetingMinutes
import datetime

# Create your tests here.
class MeetingTest (TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='Test Meeting 1.1')
        self.meeting= Meeting(meetingtitle=self.title, meetingdate=datetime('2022','03','30'), meetingtime=datetime('15:30'), meetinglocation=self.meetinglocation, meetingagenda=self.meetingagenda, )

    def test_meetingstring(self):
        self.assertEqual(str(self.type),'Test Meeting 1.1')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest (TestCase):
    def setUp(self):
        self.type=Resource(resourcetype='Example Resource')
        self.name=Resource(resourcename= 'Website')
        self.resource= Resource(resourcename=self.name, resourcetype=self.type, resourceurl='sampleurl.test.com', entrydate= datetime('2022','03','25'), userid='876', description='Testing Description')
    
    def test_resourcestring(self):
        self.assertEqual(str(self.type), 'Example Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingMinutesTest (TestCase):
    def setUp(self):
        self.type=MeetingMinutes(minutestext='Sample Minutes Text')
        self.meetingid=Meeting(meetingid='654')
        self.attendance=MeetingMinutes(attendance='Attendees')
    
    def test_minutesstring(self):
        self.assertEqual(str(self.type), 'Sample Minutes Text')
    
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

    


