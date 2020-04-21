from django.shortcuts import render
from .serializers import DepartmentsSerializer
from doctor.models import doctor
from departments.models import departments
from rest_framework.response import Response

# Create your views here.
# class DepartmentsViewSet():
# 	def get(self,request,*args):
# 		qs = []
# 		dept = []
# 		res = {}
# 		departments = departments.objects.all()
# 		for item in departments:
# 			qs.append(doctor.objects.filter(specialization__icontain=[item]).count())
# 			dept.append(str(item))
# 		for key in dept:
# 			for value in qs:
# 				res[key]=value
# 				qs.remove(value)
# 				break
# 		serializer = DepartmentsSerializer(departments,many=True)
# 		return Response({"departments":serializer.data,
# 							'count':res})

