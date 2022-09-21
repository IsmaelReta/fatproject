from datetime import datetime, timedelta
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from warehouse.models import Inventory
from warehouse.serializers import InventorySerializer
from .serializers import ProductSerializer
from django.db.models import Count, Sum
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects

    def filter_queryset(self, queryset):
        now_time_plus = datetime.now() + timedelta(days=30)
        print("time plus", now_time_plus)
        igroup = Product.objects.filter(inventory__expiration_date__gte = now_time_plus)
        sgroup = igroup.annotate(total_p = Sum('inventory__quantity'))
        return sgroup

    """
    def get_queryset(self):
        product = Product.objects.all()
        return product
    """
