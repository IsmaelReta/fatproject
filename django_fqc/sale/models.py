from django.db import models
#
from django.contrib.auth.models import User

class Sale(models.Model):
    patient = models.OneToOneField("patient.Patient",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'- Sale_ID:{self.id}'

class SaleDetail(models.Model):
    sale = models.OneToOneField("sale.Sale",on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'- SaleDetail_ID:{self.id}'