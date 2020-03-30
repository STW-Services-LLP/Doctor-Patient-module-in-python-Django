from django.db import models

# Create your models here.

class patient(models.Model):
	id = models.IntegerField(primary_key = True , unique = True)
	name = models.CharField(max_length = 100)
	city = models.CharField(max_length= 300, null = True,blank = True)
	description = models.TextField()
	admit_date = models.DateTimeField(auto_now = True)
	discharge_date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name
