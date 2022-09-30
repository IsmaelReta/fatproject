from rest_framework import viewsets
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer, \
    PatientFullSerializer, HIPost
from django.contrib.auth.models import User
from userapi.serializers import UserSerializer # noqa
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


class PatientCertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        certificate = Certificate.objects.filter(patient=patient_id)
        return certificate


class PatientHealthInsViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsurancePatientSerializer
    queryset = HealthInsurancePatient.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        hi_patient = HealthInsurancePatient.objects.filter(patient=patient_id)
        return hi_patient


class HIPost(viewsets.ModelViewSet):
    serializer_class = HIPost

    def get_queryset(self):
        hipost = HealthInsurancePatient.objects.all()
        return hipost


class PatientUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        patient_user = User.objects.filter(patient=patient_id)
        return patient_user


class PatientFullViewSet(viewsets.ModelViewSet):
    serializer_class = PatientFullSerializer

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient