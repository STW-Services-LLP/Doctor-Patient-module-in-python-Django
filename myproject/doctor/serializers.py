from .models import Doctor,d_experience
from rest_framework import serializers

#Making serializers to convert queryset datatype to native python datatypes that can be easily rendered into JSON or other content types. 

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user_id','first_name', 'last_name','phone','gender','age','email','address','city','country','description','specialization','highestqualification']
        #read_only_fields=['user_id']
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
#Doctor Experience Serializer
class d_experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=d_experience
        fields=['user_id','hospital','designation','fro','to','exp_id']

#Doctor Training Serializer (can be added if required)
# class d_trainingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=d_training
#         fields=['user_id','traininghospital','trainingon','trainingdate']

# #Doctor Education Serializer
# class d_educationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=d_education
#         fields=['user_id','college','degree','educationdate','edu_id']

# #Doctor Services Serializer
# class DoctorServicesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['services']

# #Doctor Specialization Serializer
# class DoctorSpecializationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['specialization']
        
# #Doctor Membership Serializer    
# class DoctorMembershipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['membership']
