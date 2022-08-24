from django.contrib import admin
from .models import Warehouse, Product, Inventory, PurchasePlan, PurchaseDetail, Sale, SaleDetail
# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(PurchasePlan)
admin.site.register(PurchaseDetail)
admin.site.register(Sale)
admin.site.register(SaleDetail)
