from rest_framework import serializers
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from healthinsurance.serializers import HealthInsuranceSerializer
from userapi.serializers import UserSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
import base64


class UserSerializer(RegisterSerializer): # noqa
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = None

    def get_cleaned_data(self):
        super(UserSerializer, self).get_cleaned_data()
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
        fields = ['id','tutor_first_name','tutor_last_name','patient']


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


class PatientFullSerializer(serializers.ModelSerializer):
    health_insurance = HealthInsurancePatientSerializer(many=True)
    certificate = CertificateSerializer()
    tutor = TutorSerializer()
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['user', 'id', 'document_number', 'certificate', 'tutor', 'health_insurance']
