from rest_framework import serializers

from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from healthinsurance.serializers import HealthInsuranceSerializer
from userapi.serializers import UserSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User


class UserRegisterSerializer(RegisterSerializer): 
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = None

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', '')
        }

    def save(self, request):
        user = super().save(request)
        user.username = user.email
        user.save()
        return user


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    tutor_first_name = serializers.CharField(source='first_name')
    tutor_last_name = serializers.CharField(source='last_name')


    class Meta:
        model = Tutor
        fields = ['first_name', 'last_name', 'patient']


class PatientSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Patient
        fields = '__all__'




class HealthInsurancePatientSerializer(serializers.ModelSerializer):
    healthinsurance = HealthInsuranceSerializer()

    class Meta:
        model = HealthInsurancePatient
        fields = '__all__'
        # fields = ['healthinsurance', 'description']


class HIPost(serializers.ModelSerializer):

    class Meta:
        model = HealthInsurancePatient
        fields = '__all__'


# class PatientFullSerializer(serializers.ModelSerializer):
#     health_insurance = HealthInsurancePatientSerializer(many=True)
#     certificate = CertificateSerializer()
#     tutor = TutorSerializer()
#     user = UserSerializer()
#     patient_id = serializers.IntegerField(source='id')

#     class Meta:
#         model = Patient
#         fields = ['user', 'patient_id', 'document_number', 'certificate', 'tutor', 'health_insurance']
    
class PatientFullSerializer(serializers.ModelSerializer):
    health_insurance = serializers.SerializerMethodField()
    certificate = serializers.SerializerMethodField()
    tutor = serializers.SerializerMethodField()
    patient = PatientSerializer()


    # def get_certificate(self, obj):
    #         patient = PatientSerializer()
    #         print(patient.data['id'])
    #         customer_account_query = Certificate.objects.filter(id=obj.id)
    #         serializer = CertificateSerializer(customer_account_query, many=True)
    
    #         return serializer.data

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
        fields = ['id', 'username', 'first_name', 'last_name', 'patient', 'tutor', 'certificate', 'health_insurance']
    
       