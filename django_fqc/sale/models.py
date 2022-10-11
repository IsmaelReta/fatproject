from django.db import models
from django.utils.html import format_html


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
# TODO precio setear actual del producto
