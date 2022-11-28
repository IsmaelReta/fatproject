from rest_framework import viewsets, status, mixins
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from .serializers import PatientSerializer, HealthInsurancePatientSerializer, CertificateSerializer, TutorSerializer
from django.contrib.auth.models import User
from userapi.serializers import UserSerializer  # noqa
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here.
    

# *Returns certain user
class PatientViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = PatientSerializer

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        p_id = params['pk']
        user_state = self.request.user.is_superuser
        if user_state == False:
            current_user = self.request.user.id
            if int(current_user) == int(p_id):
                patient = Patient.objects.filter(user=p_id)
                serializer = PatientSerializer(patient, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            patient = Patient.objects.filter(user=p_id)
            serializer = PatientSerializer(patient, many=True)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        patient = self.request.user.patient
        patient_object = self.get_object()
        if patient == patient_object:
            data = request.data

            patient_object.document_number = data['document_number']
            patient_object.birth_date = data['birth_date']
            patient_object.province = data['province']
            patient_object.city = data['city']

            patient_object.save()

            serializer = PatientSerializer(patient_object)
            return Response(serializer.data)
        else:
            return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


    def destroy(self, request, *args, **kwargs):
        user_state = self.request.user.is_superuser
        patient = self.get_object()
        if user_state == False:
            user_patient = self.request.user.patient
            if user_patient == patient:
                patient.delete()
                return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            patient.delete()
            return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)



# *Returns tutor from certain patient
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
        user_state = self.request.user.is_superuser
        if user_state == False:
            current_patient = self.request.user.patient.id
            current_tutor = self.get_object()
            if int(current_tutor.patient.id) == int(current_patient):
                tutor = Tutor.objects.filter(id=t_id)
                serializer = TutorSerializer(tutor, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            tutor = Tutor.objects.filter(id=t_id)
            serializer = TutorSerializer(tutor, many=True)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        patient = self.request.user.patient
        tutor_object = self.get_object()
        if patient == tutor_object.patient:
            data = request.data

            tutor_object.first_name = data['first_name']
            tutor_object.last_name = data['last_name']

            tutor_object.save()

            serializer = TutorSerializer(tutor_object)
            return Response(serializer.data)
        else:
            return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        user_state = self.request.user.is_superuser
        tutor = self.get_object()
        if user_state == False:
            user_tutor = self.request.user.patient.tutor
            if user_tutor == tutor:
                tutor.delete()
                return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            tutor.delete()
            return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)




# *Returns certificate from certain patient
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
        user_state = self.request.user.is_superuser
        if user_state == False:
            current_patient = self.request.user.patient.id
            current_certificate = self.get_object()
            if int(current_certificate.patient.id) == int(current_patient):
                certificate = Certificate.objects.filter(id=c_id)
                serializer = CertificateSerializer(certificate, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            certificate = Certificate.objects.filter(id=c_id)
            serializer = CertificateSerializer(certificate, many=True)
            return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        patient = self.request.user.patient
        certificate_object = self.get_object()
        if patient == certificate_object.patient:
            data = request.data

            certificate_object.status = data['status']
            certificate_object.image = data['image']

            certificate_object.save()

            serializer = CertificateSerializer(certificate_object)
            return Response(serializer.data)
        else:
            return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        user_state = self.request.user.is_superuser
        certificate = self.get_object()
        if user_state == False:
            user_certificate = self.request.user.patient.certificate
            if user_certificate == certificate:
                certificate.delete()
                return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            certificate.delete()
            return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)




# *Returns all healthInsurances from certain patient
class HealthInsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
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
        user_state = self.request.user.is_superuser
        if user_state == False:
            current_patient = self.request.user.patient.id
            current_health = self.get_object()
            if int(current_health.patient.id) == int(current_patient):
                health = HealthInsurancePatient.objects.filter(id=h_id)
                serializer = HealthInsurancePatientSerializer(health, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            health = HealthInsurancePatient.objects.filter(id=h_id)
            serializer = HealthInsurancePatientSerializer(health, many=True)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        patient = self.request.user.patient
        healths_object = self.get_object()
        if patient == healths_object.patient:
            data = request.data

            healths_object.healthinsurance = data['healthinsurance']
            healths_object.description = data['description']
            healths_object.patient = data['patient']

            healths_object.save()

            serializer = HealthInsurancePatientSerializer(healths_object)
            return Response(serializer.data)
        else:
            return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        user_state = self.request.user.is_superuser
        health = self.get_object()
        if user_state == False:
            user_health = self.request.user.patient.healthinsurancepatient
            if user_health == health:
                health.delete()
                return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            health.delete()
            return Response({'message': 'Item has been deleted'}, status=status.HTTP_200_OK)