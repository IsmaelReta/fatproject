from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employee = models.BooleanField(null=False, default=False)
    document_number = models.CharField(max_length=8)

    def __str__(self) -> str:
        return f'{self.user} - Person_ID:{self.id}'


class HealthInsurance(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=255, default='')
    person = models.ForeignKey('users.Person', related_name='health_insurance', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - Person_ID:{self.id}'


class Certificate(models.Model):
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users/images')
    person = models.OneToOneField('users.Person', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.status} - Person_ID:{self.id}'


class Tutor(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    person = models.OneToOneField('users.Person', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - Person_ID:{self.id}'
