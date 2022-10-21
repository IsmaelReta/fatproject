from rest_framework import viewsets, status, mixins
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer, \
    PatientFullSerializer, HIPost
from django.contrib.auth.models import User
from userapi.serializers import UserSerializer # noqa
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here.


#*Returns certain user
class PatientViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        u_id = params['pk']
        current_user = self.request.user.id
        if int(current_user) == int(u_id):
            user = User.objects.filter(id=u_id)
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)






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
        t_id = params['pk']
        current_patient = self.request.user.patient.id
        current_tutor = self.get_object()
        if int(current_tutor.patient.id) == int(current_patient):
            tutor = Tutor.objects.filter(id=t_id)
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
class CertificateViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, 
                   viewsets.GenericViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects


    def get_queryset(self):
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

        serializer = CertificateSerializer(certificate_object)
        return Response(serializer.data)






#*Returns all healthInsurances from certain patient
class HealthInsViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, 
                   viewsets.GenericViewSet):
    serializer_class = HealthInsurancePatientSerializer
    queryset = HealthInsurancePatient.objects

    
    def get_queryset(self):
        hi_patient = HealthInsurancePatient.objects.all()
        return hi_patient

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        h_id = params['pk']
        current_patient = self.request.user.patient.id
        current_health = self.get_object()
        if int(current_health.patient.id) == int(current_patient):
            health = HealthInsurancePatient.objects.filter(id=h_id)
            serializer = HealthInsurancePatientSerializer(health, many=True)
            return Response(serializer.data)
        else:
            return Response({'error' : 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


    def update(self, request, *args, **kwargs):
        healths_object = self.get_object()
        data = request.data


        healths_object.healthinsurance = data['healthinsurance']   
        healths_object.description = data['description']   
        healths_object.patient = data['patient']   


        healths_object.save()

        serializer = HealthInsurancePatientSerializer(healths_object)
        return Response(serializer.data)







#*Returns all user data, including patient data
class PatientFullViewSet(viewsets.ModelViewSet):
    serializer_class = PatientFullSerializer
    
    
    def get_queryset(self):
        patient = Patient.objects.all()
        return patient



    def list(self, request):
        user_state = request.user.is_superuser
        if user_state == True:
            user = User.objects.all()
            serializer = PatientFullSerializer(user, many = True)
            return Response(serializer.data)
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


