from django.db import models
#
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    document_number = models.CharField(max_length=8)

    def __str__(self) -> str:
        return f'{self.user} - Patient_ID:{self.id}'


class HealthInsurance(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=255, default='')
    patient = models.ForeignKey('patient.Patient', related_name='health_insurance', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - Patient_ID:{self.id}'


class Certificate(models.Model):
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='patient/images')
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.status} - Patient_ID:{self.id}'


class Tutor(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - Patient_ID:{self.id}'
