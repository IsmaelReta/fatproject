from django.db import models
from django.utils.html import format_html
from django.db.models.signals import post_save, pre_save, pre_delete
from warehouse.models import Warehouse, Inventory


class Sale(models.Model):
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aceptado'),
        ('C', 'Cancelado'),
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='P')

    def __str__(self) -> str:
        return f'- Sale_ID:{self.id}'

    def status_label(self,):
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
            label_text = "imposible status"

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
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    # expiration_date = models.DateField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'- SaleDetail_ID:{self.id}'

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     super(SaleDetail, self).save()


def detail_post_save(sender, instance, created, *args, **kwargs):
    pass


post_save.connect(detail_post_save, sender=SaleDetail)


def detail_pre_save(sender, instance: SaleDetail, *args, **kwargs):
    previous = SaleDetail.objects.get(id=instance.id)
    new = instance
    if previous.amount == new.amount:                               # are there amount changes?
        return print("no amount changes", previous.amount, new.amount)
    elif previous.amount > new.amount:                              # reduced amount, add in inventory
        print("reduced amount")
        change = previous.amount - new.amount
        if Inventory.objects.get(id=new.product.id).id == new.product.id:   # add to existing inventory
            print("add to inventory")
            inventory = Inventory.objects.get(id=new.product.id)
            inventory.quantity += change
            inventory.save()
        else:                                                              # create inventory with poduct
            print("create inventory")
            inv = Inventory(product_id=new.product.id, quantity=change, type=' ', warehouse_id=1)
            inv.save()
    elif previous.amount < new.amount:                      # increased amount, remove from inventory
        print("increased amount")
        change = new.amount - previous.amount
        inventory = Inventory.objects.get(id=new.product.id)
        if inventory.quantity == change:                    # if new equal to saved delete inventory
            print("delete inventory")
            inventory.delete()
            """
        elif inventory.quantity < change
        else:
            if inventory.quantity > change:
                inventory.quantity -= change                    # remove from inventory
                inventory.save()
                print("remove from inventory", inventory.id)
            else:
                while change != 0:

                    inventory = Inventory.objects.get(id=new.product.id)
                    change -= inventory.quantity
                    inventory.delete()

pre_save.connect(detail_pre_save, sender=SaleDetail)"""

# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Sale, SaleDetail


