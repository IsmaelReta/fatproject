from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient


class HealthInsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsurancePatientSerializer

    def get_queryset(self):
        health_insurance = HealthInsurancePatient.objects.all()
        return health_insurance


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        certificate = Certificate.objects.all()
        return certificate


class PatientTutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer  
    queryset = Tutor.objects  
    
    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        tutors = Tutor.objects.filter(patient=patient_id)
        return tutors
