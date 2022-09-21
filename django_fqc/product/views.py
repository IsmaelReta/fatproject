from datetime import datetime, timedelta
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from warehouse.models import Inventory
from warehouse.serializers import InventorySerializer
from .serializers import ProductSerializer
from django.db.models import lookups

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects

    def filter_queryset(self, queryset):
        now_time_plus = datetime.now() + timedelta(days=30)
        print("time plus", now_time_plus)
        inventory = Inventory.objects.filter(expiration_date__gte=now_time_plus)
        return inventory

    """
    def get_queryset(self):
        product = Product.objects.all()
        return product
    """
