from django.db import models


class Sale(models.Model):
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)

    PENDIENTE = 'Pendiente'
    ACEPTADO = 'Aceptado'
    CANCELADO = 'Cancelado'
    STATUS_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (ACEPTADO, 'Aceptado'),
        (CANCELADO, 'Cancelado'),
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=PENDIENTE)

    def __str__(self) -> str:
        return f'- Sale_ID:{self.id}'


class SaleDetail(models.Model):
    sale = models.ForeignKey("sale.Sale", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    expiration_date = models.DateField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'- SaleDetail_ID:{self.id}'
