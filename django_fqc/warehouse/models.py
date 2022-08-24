from django.db import models
from ..users.models import Person
# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=64)


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Inventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    type = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)


class PurchasePlan(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class PurchaseDetail(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    plan_id = models.ForeignKey(PurchasePlan, on_delete=models.DO_NOTHING)


class Sale(models.Model):
    persona_id = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class SaleDetail(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
