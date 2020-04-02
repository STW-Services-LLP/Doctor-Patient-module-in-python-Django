from django.db import models
from django.db.models import Q

# Create your models here.

class PatientManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(description__icontains=query)|
                         Q(city__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs



class patient(models.Model):
	id = models.IntegerField(primary_key = True , unique = True)
	name = models.CharField(max_length = 100)
	city = models.CharField(max_length= 300, null = True,blank = True)
	description = models.TextField()
	admit_date = models.DateTimeField(auto_now_add = True)
	role = models.CharField(max_length = 50 ,blank = True ,default = '')
	discharge_date = models.DateTimeField(auto_now = True)

	objects = PatientManager()

	# def __str__(self):
	# 	return self.name


