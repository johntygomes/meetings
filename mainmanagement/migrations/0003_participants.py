# Generated by Django 3.1.7 on 2021-03-01 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainmanagement', '0002_remove_meeting_meetingdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participantName', models.CharField(max_length=450)),
                ('participantEmail', models.CharField(max_length=450)),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainmanagement.meeting')),
            ],
        ),
    ]
