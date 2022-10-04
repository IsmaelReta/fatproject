from rest_framework import viewsets, status
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer, \
    PatientFullSerializer, HIPost
from django.contrib.auth.models import User
from userapi.serializers import UserSerializer # noq
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
# Create your views here.


#*Returns all patients
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient


# class HealthInsuranceViewSet(viewsets.ModelViewSet):
#     serializer_class = HealthInsurancePatientSerializer

#     def get_queryset(self):
#         health_insurance = HealthInsurancePatient.objects.all()
#         return health_insurance


# class CertificateViewSet(viewsets.ModelViewSet):
#     serializer_class = CertificateSerializer

#     def get_queryset(self):
#         certificate = Certificate.objects.all()
#         return certificate

#*Returns tutor from certain patient
class PatientTutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer  
    queryset = Tutor.objects  
    
    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        tutors = Tutor.objects.filter(patient=patient_id)
        return tutors

#*Returns certificate from certain patient
class PatientCertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        certificate = Certificate.objects.filter(patient=patient_id)
        return certificate

#*Returns all healthInsurances from certain patient
class PatientHealthInsViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsurancePatientSerializer
    queryset = HealthInsurancePatient.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        hi_patient = HealthInsurancePatient.objects.filter(patient=patient_id)
        return hi_patient

#*Returns all health insurances from all patients
class HIPost(viewsets.ModelViewSet):
    serializer_class = HIPost

    def get_queryset(self):
        hipost = HealthInsurancePatient.objects.all()
        return hipost

#*Returns user data from a patient
class PatientUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects

    def filter_queryset(self, queryset):
        patient_id = self.kwargs["patient_id"]
        patient_user = User.objects.filter(patient=patient_id)
        return patient_user

#* returns all users with its data, including patients data
class PatientFullViewSet(viewsets.ModelViewSet):
    serializer_class = PatientFullSerializer

    def get_queryset(self):
        user = self.request.user
        user_state = user.is_authenticated
        if user_state == True:
            patient = Patient.objects.all()
            return patient
        else:
            raise ValidationError(detail='Superuser Required') 

    # def get(self, request):
    #     user_state = request.user.is_superuser
    #     if user_state == True:
    #         serializer = PatientFullSerializer(data = request.data)
    #         if serializer.is_valid():
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({'error' : 'Authorization Required'}, status=status.HTTP_401_UNAUTHORIZED)