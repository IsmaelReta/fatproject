from django.db import models

# Create your models here.
class HealthInsurance(models.Model):
    name = models.CharField("name", max_length=50)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.name}'

class Product(models.Model):
    name = models.CharField("name", max_length=50)
    expiration_date = models.DateField()
    sale_avaiable = models.BooleanField(null=False)
    stock = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.name} {self.expiration_date} {self.stock} {self.price}'


class Province(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.name}'

class Address(models.Model):
    location = models.CharField("location", max_length=50)
    neighborhood = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    id_province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.location} {self.neighborhood}'

class User(models.Model):
    last_name = models.CharField("last_n", max_length=100)
    first_name = models.CharField("first_n", max_length=100)
    dni = models.DecimalField("dni", max_digits=8, decimal_places=0)
    email = models.CharField("email", max_length=100)
    normal = models.BooleanField("disability certificate",null=False)
    id_hi = models.OneToOneField("HealthInsurance", on_delete=models.CASCADE)
    id_home = models.ForeignKey("Address", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.last_name} {self.first_name}'


class OrderDetail(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    #id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return f'ID: {self.id} - {self.amount} {self.id_product} {self.amount_price}'

class Order(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_OrderDetail = models.ManyToManyField(OrderDetail)
    def __str__(self) -> str:
        return f'ID: {self.id}'
