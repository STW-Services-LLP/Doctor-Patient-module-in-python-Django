from django.db import models

# Create your models here.
class departments(models.Model):
	# d_name = models.ForeignKey(doctor ,null=True ,on_delete = models.CASCADE)
	department = models.CharField(max_length = 100 ,blank = True ,null = True)


	def __str__(self):
		return str(self.department)




