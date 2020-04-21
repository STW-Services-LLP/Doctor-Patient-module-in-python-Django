from .models import departments
from rest_framework import serializers

#Making departments serializer to convert queryset datatype to native python datatypes that can be easily rendered into JSON or other content types. 

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = departments
        fields = ['name']

        