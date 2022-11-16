from rest_framework import serializers
from healthinsurance.models import HealthInsurance
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from healthinsurance.serializers import HealthInsuranceSerializer
# from userapi.serializers import UserSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
# from django.contrib.auth.models import User


class UserRegisterSerializer(RegisterSerializer): 
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = None

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', '')
        }

    def save(self, request):
        user = super().save(request)
        user.username = user.email
        user.save()
        return user


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ['first_name', 'last_name', 'patient']



class HealthInsurancePatientSerializer(serializers.ModelSerializer):
    
    health_name = serializers.SerializerMethodField()

    def get_health_name(self, obj):
            health = HealthInsurance.objects.filter(name=obj.healthinsurance)
            serializer = HealthInsuranceSerializer(health, many=True)

            return serializer.data


    class Meta:
        model = HealthInsurancePatient
        fields = ['id', 'healthinsurance', 'description', 'patient', 'health_name']


class PatientSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Patient
        fields = ['user', 'id', 'document_number', 'birth_date', 'city', 'province']
