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
        now_time_plus = datetime.now() + timedelta(days=30)
        products_date_filtered = Product.objects.filter(inventory__expiration_date__gte=now_time_plus)
        products_with_quantity = products_date_filtered.annotate(total_products=Sum('inventory__quantity'))
        return products_with_quantity
