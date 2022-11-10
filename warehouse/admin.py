from django.contrib import admin
from .models import Warehouse, Inventory
# Register your models here.


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'warehouse')


admin.site.register(Warehouse)
admin.site.register(Inventory, InventoryAdmin)
