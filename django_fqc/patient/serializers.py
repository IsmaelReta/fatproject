from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, HealthInsurancePatient, Certificate, Tutor


class HealthInsurancePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurancePatient
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    """
    health_insurance = HealthInsuranceSerializer(many=True)
    certificate = CertificateSerializer()
    tutor = TutorSerializer()
    user = UserSerializer()
    """

    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ['user', 'id', 'document_number', 'certificate', 'tutor', 'health_insurance']
