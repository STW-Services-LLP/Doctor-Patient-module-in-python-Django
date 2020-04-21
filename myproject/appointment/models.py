from django.db import models

# Create your models here.

class Appointment_Booking(models.Model):
	first_name = models.CharField(max_length = 50 , blank = True , default = '' )
	last_name = models.CharField(max_length = 50 , blank = True , default = '')
	email = models.CharField(max_length = 50 ,blank = True ,default = '')
	phone = models.CharField(max_length = 13 ,blank = True ,default = '')
	address = models.CharField(max_length = 50 ,blank = True , default = '')
	city = models.CharField(max_length = 50 ,blank = True ,default = '')
	country = models.CharField(max_length = 50 ,blank = True ,default = '' )
	description = models.CharField(max_length = 100 ,blank = True ,default = '')
	doctor_name = models.CharField(max_length = 50 ,blank = True ,default = '')
	schedule_time =models.CharField(max_length = 50 ,blank = True ,default = '')
	appointment = models.CharField(max_length = 50 ,blank = True ,default = '')
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.first_name
