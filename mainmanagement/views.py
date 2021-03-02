from django.shortcuts import render
from django.http import HttpResponse
from .models import Meeting,Participants
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Create your views here.
def home(request):
    meetings=Meeting.objects.all()
    return render(request,"home.html",{'meetings':meetings})

currentMeetingId=0
subject=''
body=''
fromaddr = "YOUR_EMAIL"

def submitMeetingData(request):
    global currentMeetingId
    global subject
    if request.method=='POST':
        meeting=Meeting()
        meeting.meetingSubject=request.POST.get('meetingSubject')
        meeting.meetingDate=request.POST.get('meetingDate')
        meeting.meetingTime = request.POST.get('meetingTime')
        meeting.save()
        currentMeetingId = meeting.id

        subject=request.POST.get('meetingSubject')+' on '+str(request.POST.get('meetingDate'))+' at '+str(request.POST.get('meetingTime'))
        return render(request,"submitMeetingData.html",{'meeting':meeting})

def submitParticipants(request):
    global currentMeetingId
    global subject
    global body
    if request.method=='POST':
        participant1=Participants()
        participant1.participantName=request.POST.get('employeeName1')
        participant1.participantEmail=request.POST.get('employeeEmail1')
        participant1.participantMeeting = currentMeetingId
        participant1.save()
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        toaddr=request.POST.get('employeeEmail1')
        msg['To'] = request.POST.get('employeeEmail1')
        msg['Subject']=subject
        body="Hello "+request.POST.get('employeeName1')+" ..Do Not Be Late For Above Meeting"
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "YOUR_PASSWORD")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()


        participant2 = Participants()
        participant2.participantName=request.POST.get('employeeName2')
        participant2.participantEmail=request.POST.get('employeeEmail2')
        participant2.participantMeeting = currentMeetingId
        participant2.save()
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        toaddr=request.POST.get('employeeEmail2')
        msg['To'] = request.POST.get('employeeEmail2')
        msg['Subject']=subject
        body="Hello "+request.POST.get('employeeName2')+" ..Do Not Be Late For Above Meeting"
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "YOUR_PASSWORD")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        participant3 = Participants()
        participant3.participantName=request.POST.get('employeeName3')
        participant3.participantEmail=request.POST.get('employeeEmail3')
        participant3.participantMeeting = currentMeetingId
        participant3.save()
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        toaddr=request.POST.get('employeeEmail3')
        msg['To'] = request.POST.get('employeeEmail3')
        msg['Subject']=subject
        body="Hello "+request.POST.get('employeeName3')+" ..Do Not Be Late For Above Meeting"
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "YOUR_PASSWORD")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        return render(request, "submitParticipants.html")
    #return render(request, "submitParticipants.html")
