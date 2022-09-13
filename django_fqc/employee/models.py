from django.db import models
#
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user} - Employee_ID:{self.id}'
