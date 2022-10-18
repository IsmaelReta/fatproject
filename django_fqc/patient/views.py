from rest_framework import viewsets, status, mixins
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer, \
    PatientFullSerializer, HIPost
from django.contrib.auth.models import User
from userapi.serializers import UserSerializer # noq
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
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
class TutorViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, 
                   viewsets.GenericViewSet):
    serializer_class = TutorSerializer  
    queryset = Tutor.objects  
    

    def get_queryset(self):
        tutors = Tutor.objects.all()
        return tutors
    
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        p_id = params['pk']
        currentPatient = self.request.user.patient.id
        if int(currentPatient) == int(p_id):
            tutor = Tutor.objects.filter(patient=p_id)
            serializer = TutorSerializer(tutor, many=True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


    def update(self, request, *args, **kwargs):
        tutor_object = self.get_object()
        data = request.data


        tutor_object.first_name = data['first_name']   
        tutor_object.last_name = data['last_name']   


        tutor_object.save()

        serializer = TutorSerializer(tutor_object)
        return Response(serializer.data)




#*Returns certificate from certain patient
class PatientCertificateViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, 
                   viewsets.GenericViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects

    #?only can access to own certificates
    def get_queryset(self):
        # pk = self.kwargs["pk"]
        # certificate = Certificate.objects.filter(id=pk)
        certificate = Certificate.objects.all()
        return certificate
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        c_id = params['pk']
        current_patient = self.request.user.patient.id
        current_certificate = self.get_object()
        if int(current_certificate.patient.id) == int(current_patient):
            certificate = Certificate.objects.filter(id=c_id)
            serializer = CertificateSerializer(certificate, many=True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        certificate_object = self.get_object()
        data = request.data


        certificate_object.status = data['status']   
        certificate_object.image = data['image']   


        certificate_object.save()

        serializer = TutorSerializer(certificate_object)
        return Response(serializer.data)




#*Returns all healthInsurances from certain patient
class PatientHealthInsViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsurancePatientSerializer
    queryset = HealthInsurancePatient.objects

    #?only can access to own health insurances
    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        hi_patient = HealthInsurancePatient.objects.filter(patient=patient_id)
        return hi_patient




#*Returns all health insurances from all patients
class HIPost(viewsets.ModelViewSet):
    serializer_class = HIPost

    def get_queryset(self):
        hipost = HealthInsurancePatient.objects.all()
        return hipost




#*Returns user data from request user
class PatientUserViewSet(viewsets.ModelViewSet):
    serializer_class = PatientFullSerializer

    #?only can acces to own data
    def get_queryset(self):
        user = self.request.user
        patient_user = Patient.objects.filter(user=user)
        return patient_user




#*Returns all users with its data, including patients data
class PatientFullViewSet(viewsets.ModelViewSet):
    serializer_class = PatientFullSerializer
    
    
    def get_queryset(self):
        patient = Patient.objects.all()
        return patient



    def list(self, request):
        user_state = request.user.is_superuser
        if user_state == True:
            serializer = PatientFullSerializer(data = request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error' : 'Authorization Required'}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        p_id = params['pk']
        currentPatient = self.request.user.patient.id
        print(params['pk'])
        if int(currentPatient) == int(p_id):
            patient = Patient.objects.filter(id=p_id)
            serializer = PatientFullSerializer(patient, many=True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


