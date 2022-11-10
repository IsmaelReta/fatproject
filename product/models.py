from django.db import models
from django.utils.html import format_html
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.CharField(max_length=256)
    MARKET_CHOICES = [
        ('Y', 'Permitido en Market'), # noqa
        ('N', 'No permitido en Market'), # noqa
    ]
    market = models.CharField(max_length=23, choices=MARKET_CHOICES, default='N')

    def __str__(self) -> str:
        return f'{self.name}-ID:{self.id}  Precio:{self.price}' # noqa

    def image(self):
        return format_html(
            f'<a href="{self.image_link}" target="_blank">'
            f'<img src="{self.image_link}"'
            f' width="100px" height="50px"> </a>'
        )

    def stock(self):
        inventories = self.inventory_set.filter(product_id=self.id)
        quantity = 0
        for inventory in inventories:
            quantity += inventory.quantity
        return quantity
