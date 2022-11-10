from django.contrib import admin
from .models import Product
from .views import ProductViewSet
from django.db.models import Sum
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'market', 'stock', 'image')
    readonly_fields = ('stock', 'image')
    list_filter = ('market', )


admin.site.register(Product, ProductAdmin)
