from django.db import models
from django.db.models import Q
from departments.models import departments


# Create your models here.
class DoctorManager(models.Manager):
	def search(self, query=None):
		qs = self.get_queryset()
		if query is not None:
			or_lookup = (Q(first_name__icontains=query) | 
						 Q(country__icontains=query)|
						 Q(city__icontains=query)
						)
			qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
		return qs


class doctor(models.Model):
	# user_id = models.CharField(max_length = 100 , blank = True , default = '')
	first_name = models.CharField(max_length = 50 , blank = True , default = '')
	last_name = models.CharField(max_length = 50 ,blank = True ,default = '')
	role = models.CharField(max_length = 50 ,blank = True ,default = '')
	phone = models.CharField(max_length = 13 ,blank = True ,default = '')
	gender = models.CharField(max_length = 20 , blank = True ,default = '')
	age = models.CharField(max_length = 10 ,blank = True , default = '')
	email = models.CharField(max_length = 100 ,blank = True , default = '')
	address = models.CharField(max_length = 100 ,blank = True ,default = '')
	department = models.ForeignKey(departments ,null = True ,on_delete = models.CASCADE)
	city = models.CharField(max_length = 50 ,blank = True ,default = '')
	country = models.CharField(max_length = 50 ,blank = True ,default = '' )
	description = models.TextField(max_length = 1000 , blank = True ,default = '')
	specialization = models.CharField(max_length = 100 ,blank = True ,default = '')
	highestqualification = models.CharField(max_length = 100 ,blank = True ,default = '')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = DoctorManager()

	def __str__(self):
		return self.first_name
			

 
 