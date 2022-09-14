from django.db import models

# Create your models here.


class HealthInsurance(models.Model):
    name = models.CharField(max_length=25, default='')
    
    def __str__(self) -> str:
        return f'{self.name} - Patient_ID:{self.id}'
