from rest_framework import serializers
from django.contrib.auth.models import User
from patient.serializers import (PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer)
from patient.models import (Patient, HealthInsurancePatient, Certificate, Tutor)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserFullSerializer(serializers.ModelSerializer):
    health_insurance = serializers.SerializerMethodField()
    certificate = serializers.SerializerMethodField()
    tutor = serializers.SerializerMethodField()
    patient = PatientSerializer()



    def get_health_insurance(self, obj):
            pat = Patient.objects.filter(user=obj)
            customer_account_query = HealthInsurancePatient.objects.filter(patient__in=pat)
            serializer = HealthInsurancePatientSerializer(customer_account_query, many=True)
    
            return serializer.data

    def get_certificate(self, obj):
            pat = Patient.objects.filter(user=obj)
            customer_account_query = Certificate.objects.filter(patient__in=pat)
            serializer = CertificateSerializer(customer_account_query, many=True)
    
            return serializer.data

    def get_tutor(self, obj):
            pat = Patient.objects.filter(user=obj)
            customer_account_query = Tutor.objects.filter(patient__in=pat)
            serializer = TutorSerializer(customer_account_query, many=True)
    
            return serializer.data


    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'patient', 'tutor', 'certificate', 'health_insurance']