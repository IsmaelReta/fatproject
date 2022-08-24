from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employee = models.BooleanField(null=False, default=False)
    document_number = models.CharField(max_length=8)


class HealthInsurance(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=255, default='')
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)


class Certificate(models.Model):
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users/images')


class Tutor(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
