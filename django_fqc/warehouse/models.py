from django.db import models
# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.name} - ID:{self.id}'


class Inventory(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    # expiration_date = models.DateField()
    type = models.CharField(max_length=255)
    warehouse = models.ForeignKey('warehouse.Warehouse', related_name='inventory', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.product} - Inventory_ID:{self.id}'
