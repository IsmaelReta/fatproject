from datetime import datetime, timedelta
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from warehouse.models import Inventory
from warehouse.serializers import InventorySerializer
from .serializers import ProductSerializer
from django.db.models import Sum
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects

    def filter_queryset(self, queryset):
        product_market_filer = Product.objects.filter(market='Y')
        products_with_quantity = product_market_filer.annotate(total_products=Sum('inventory__quantity'))
        return products_with_quantity
