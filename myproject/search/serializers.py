from rest_framework import serializers
from search.models import patient
from doctor.models import doctor



class DoctorSerilizers(serializers,ModelSerializer):
	class Meta:
		model = doctor
		fields = ['name','city','department']

class PatientSerializers(serializers,ModelSerializer):
	Doctor = DoctorSerilizers()

	class Meta:
		model = patient
		fields = ['name','city','department',]		