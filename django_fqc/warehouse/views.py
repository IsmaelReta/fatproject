from django.shortcuts import render
from rest_framework import viewsets
from .models import Warehouse, Inventory
from .serializers import WarehouseSerializer, InventorySerializer
# Create your views here.


class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        warehouse = Warehouse.objects.all()
        return warehouse


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer

    def get_queryset(self):
        inventory = Inventory.objects.all()
        return inventory
