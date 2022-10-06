from rest_framework import serializers
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
from healthinsurance.serializers import HealthInsuranceSerializer
from userapi.serializers import UserSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer


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

    class Meta:
        model = Tutor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    # firstn = serializers.CharField()
    # lastn = serializers.CharField()

    class Meta:
        model = Patient
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     return instance



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
    patient_id = serializers.IntegerField(source='id')

    class Meta:
        model = Patient
        fields = ['user', 'patient_id', 'document_number', 'certificate', 'tutor', 'health_insurance']

    