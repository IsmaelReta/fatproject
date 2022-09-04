from django.shortcuts import render
from rest_framework import viewsets
# from .serializers import AllSerializer
from .models import Person, HealthInsurance, Certificate, Tutor
from .serializers import PersonSerializer, HealthInsuranceSerializer, CertificateSerializer, TutorSerializer
# Create your views here.


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        person = Person.objects.all()
        return person


class HealthInsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsuranceSerializer

    def get_queryset(self):
        health_insurance = HealthInsurance.objects.all()
        return health_insurance


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        certificate = Certificate.objects.all()
        return certificate


class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer

    def get_queryset(self):
        tutor = Tutor.objects.all()
        return tutor
"""
class UserGetView(viewsets.ModelViewSet):
    serializer_class = AllSerializer
    queryset = Person.objects.all()
"""
