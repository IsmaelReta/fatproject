from django.db import models

# Create your models here.


class Purchase(models.Model):
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.date} - ID:{self.id}'


class PurchaseDetail(models.Model):
    product = models.OneToOneField('product.Product', on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    purchase = models.ForeignKey('purchase.Purchase', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.product} - ID:{self.id}'
