from rest_framework import serializers
from .models import Warehouse, Inventory


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(many=True)

    class Meta:
        model = Warehouse
        # fields = '__all__'
        fields = ['name', 'inventory']
