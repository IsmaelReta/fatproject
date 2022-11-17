from rest_framework import serializers
from django.contrib.auth.models import User
from patient.serializers import (PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer)
from patient.models import (Patient, HealthInsurancePatient, Certificate, Tutor)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class UserFullSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'patient']

