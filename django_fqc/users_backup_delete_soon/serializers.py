from rest_framework import serializers
from .models import Person, HealthInsurance, Certificate, Tutor
from django.contrib.auth.models import User


class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
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


class PersonSerializer(serializers.ModelSerializer):
    health_insurance = HealthInsuranceSerializer()
    certificate = CertificateSerializer()
    tutor = TutorSerializer()
    user = UserSerializer()

    class Meta:
        model = Person
        fields = ['user', 'id', 'user', 'employee', 'document_number', 'certificate', 'tutor', 'health_insurance']
