from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	
	is_patient = models.BooleanField(default = False , verbose_name="Patient")
	is_doctor = models.BooleanField(default = False ,verbose_name="Doctor")
class Patient(models.Model):
	user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	user.is_patient = True
	pid = models.AutoField(unique = True ,primary_key=True)


class Doctor(models.Model):
	upin = models.AutoField(primary_key = True , unique = True)
	user = models.OneToOneField(CustomUser , on_delete = models.CASCADE)
	user.is_doctor = True
	experience = models.CharField(max_length = 30)

# class Role(models.Model):
# 	DOCTOR = 1
# 	PATIENT = 2
# 	ROLE_CHOICES = (
# 		(DOCTOR = 'doctor'),
# 		(PATIENT = 'patient'),
# 		)		

# 	id = models.PositiveSmallIntegerField(choices = ROLE_CHOICES ,primary_key = True)