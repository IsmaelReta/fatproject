from django.shortcuts import render
from rest_framework import viewsets

from .models import Patient, HealthInsurance, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsuranceSerializer, CertificateSerializer, TutorSerializer
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient

class HealthInsuranceViewSet(viewsets.ViewSet):
    serializer_class = HealthInsuranceSerializer

    def get_queryset(self):
        health_insurance = HealthInsurance.objects.all()
        return health_insurance


class CertificateViewSet(viewsets.ViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        certificate = Certificate.objects.all()
        return certificate
    
class TutorViewSet(viewsets.ViewSet):
    serializer_class = TutorSerializer

    def get_queryset(self):
        tutor = Tutor.objects.all()    
        return tutor
    
