from django.db import models
import base64
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    document_number = models.CharField(max_length=8)
    birth_date = models.DateField(null=True)
    province = models.CharField(max_length=25)
    city = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.user} - Patient_ID:{self.id}'


class HealthInsurancePatient(models.Model):
    healthinsurance = models.ForeignKey('healthinsurance.HealthInsurance', on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, default='')
    patient = models.ForeignKey('patient.Patient', related_name='health_insurance', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.healthinsurance.name} - Patient_ID:{self.patient.id}'


class Certificate(models.Model):
    image_binary = models.BinaryField(editable=True, null=True)
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'Patient_ID:{self.id}'


class Tutor(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - Patient_ID:{self.id}'
