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


class BlobCertificate(models.Model):
    blob = models.TextField(db_column='data', default=' ', blank=True)

    def set_data(self, data):
        self.blob = base64.encodebytes(data)

    def get_data(self):
        return base64.decodebytes(self.blob)

    data = property(get_data, set_data)

    image = models.ImageField(upload_to=set_data, default='patients/certificates/default_certificate.jpg')
    certificate = models.OneToOneField('patient.Certificate', on_delete=models.CASCADE)


class Certificate(models.Model):
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='patients/certificates')
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.status} - Patient_ID:{self.id}'


class Tutor(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    patient = models.OneToOneField('patient.Patient', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - Patient_ID:{self.id}'
