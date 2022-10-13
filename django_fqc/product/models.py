from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.name} - ID:{self.id}'
