from django.db import models
from django.utils.html import format_html
from django.db.models.signals import post_save, pre_save, post_delete
from warehouse.models import Warehouse, Inventory
from product.models import Product


class Sale(models.Model):
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('P', 'Pendiente'), # noqa
        ('A', 'Aceptado'), # noqa
        ('C', 'Cancelado'), # noqa
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='P')
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'- Sale_ID:{self.id} '

    def status_label(self, ):
        status = self.status
        if status == 'P':
            style = "color:yellow"
            label_text = self.STATUS_CHOICES[0][1]
        elif status == 'A':
            style = "color:green"
            label_text = self.STATUS_CHOICES[1][1]
        elif status == 'C':
            style = "color:red"
            label_text = self.STATUS_CHOICES[2][1]
        else:
            style = "color:red"
            label_text = "impossible status"

        return format_html(
            f'<span style="{style}">{label_text}</span>'
        )

    '''match status:
            case 'P':
                label = "badge badge-warning"
                label_text = self.STATUS_CHOICES[0][1]
                return label, label_text
            case 'A':
                label = "badge badge-success"
                label_text = self.STATUS_CHOICES[1][1]
                return label, label_text
            case 'C':
                label = "badge badge-danger"
                label_text = self.STATUS_CHOICES[2][1]
                return label, label_text'''


class SaleDetail(models.Model):
    sale = models.ForeignKey("sale.Sale", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name='product_data')
    # expiration_date = models.DateField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'- Detail_ID:{self.id}'


def detail_post_save(sender, instance, created, *args, **kwargs):
    if created is True:
        product = Product.objects.get(id=instance.product.id)
        instance.price = product.price
        instance.save()


post_save.connect(detail_post_save, sender=SaleDetail)


def detail_pre_save(instance: SaleDetail, *args, **kwargs):
    new = instance
    new.amount = int(new.amount)
    detail_exist = SaleDetail.objects.filter(id=instance.id).first()
    if detail_exist is None:
        product = Product.objects.get(id=new.product.id)
        previous = SaleDetail(product_id=new.product.id, amount=0, price=product.price)
    else:
        previous = SaleDetail.objects.get(id=instance.id)

    if previous.amount == new.amount:  # are there amount changes?
        return print("no amount changes", previous.amount, new.amount)
    elif previous.amount > new.amount:  # reduced amount, add in inventory
        # print("reduced amount")
        change = previous.amount - new.amount
        if Inventory.objects.filter(product_id=new.product.id).first().id == new.product.id:  # ad to existing inventory
            # print("add to inventory")
            inventory = Inventory.objects.filter(product_id=new.product.id).first()
            inventory.quantity += change
            inventory.save()
        else:  # create inventory with product
            # print("create inventory")
            inv = Inventory(product_id=new.product.id, quantity=change, type=' ', warehouse_id=1)
            inv.save()
    elif previous.amount < new.amount:  # increased amount, remove from inventory
        # print("increased amount")
        change = new.amount - previous.amount
        while change != 0:
            # print("inside the loop!", new.product.id)
            inventory = Inventory.objects.filter(product_id=new.product.id).first()
            # print("inside the loop!!!", new.product.id, inventory)
            if inventory.quantity == change:  # if new equal to saved delete inventory
                # print("delete inventory")
                inventory.delete()
                change = 0
            elif inventory.quantity > change:
                inventory.quantity -= change  # if inv greater than change remove from inventory
                inventory.save()
                # print("remove from inventory", inventory.id)
                change = 0
            else:  # inv less than change, delete inv and update change
                change -= inventory.quantity
                inventory.delete()


pre_save.connect(detail_pre_save, sender=SaleDetail)


def detail_post_delete(instance: SaleDetail, *args, **kwargs):
    change = instance.amount
    inventory = Inventory.objects.filter(product_id=instance.product.id).first()
    if inventory.id == instance.product.id:
        # ad to existing inventory
        print("add to inventory")
        inventory.quantity += change
        inventory.save()
    else:  # create inventory with product
        print("create inventory")
        inv = Inventory(product_id=instance.product.id, quantity=change, type=' ', warehouse_id=1)
        inv.save()


post_delete.connect(detail_post_delete, sender=SaleDetail)
