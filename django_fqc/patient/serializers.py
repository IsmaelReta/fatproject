from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, HealthInsurance, Certificate, Tutor

class HealthInsuranceSerializer(serializers.Serializer):
    class Meta:
        model = HealthInsurance
        fields = '__all__'

class CertificateSerializer(serializers.Serializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class TutorSerializer(serializers.Serializer):
     class Meta:
        model = Tutor
        fields = '__all__'


class UserSerializer(serializers.Serializer):
     class Meta:
        model =  User
        fields = '__all__'

class PatientSerializer(serializers.Serializer):
    healt_insurance = HealthInsuranceSerializer()
    certificate = CertificateSerializer()
    tutor = TutorSerializer()
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['user', 'id', 'user', 'employee', 'document_number', 'certificate', 'tutor', 'health_insurance']