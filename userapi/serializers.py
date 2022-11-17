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

        # def update(self, instance, validated_data):
        #         patient = validated_data.get('patient')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.patient.document_number = patient.get('document_number')
        #         instance.user.save()

        #         print("hey")
        #         return instance

#     def update(self, instance, validated_data):
#         health_insurance = validated_data.pop('health_insurance')
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)

#         return instance
