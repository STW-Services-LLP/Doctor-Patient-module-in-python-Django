# Generated by Django 3.0.4 on 2020-04-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_booking',
            name='doctor_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='appointment_booking',
            name='schedule_time',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]