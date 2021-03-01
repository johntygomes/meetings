from django.db import models

# Create your models here.
class Meeting(models.Model):
    meetingSubject=models.CharField(max_length=450)
    meetingDate=models.DateField(auto_now=False,auto_now_add=False)
    meetingTime=models.TimeField(auto_now=False,auto_now_add=False)

class Participants(models.Model):
    participantName=models.CharField(max_length=450)
    participantEmail = models.CharField(max_length=450)
    participantMeeting = models.IntegerField()
