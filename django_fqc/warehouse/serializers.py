from rest_framework import serializers
from .models import Warehouse, Inventory


class InventorySerializer(serializers.ModelSerializer):
    total_p = serializers.IntegerField()
    p = serializers.IntegerField()

    class Meta:
        model = Inventory
        fields =  ['products', 'quantity', 'expiration_date', 'type', 'warehouse', 'total_p', 'p']


class WarehouseSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(many=True)

    class Meta:
        model = Warehouse
        # fields = '__all__'
        fields = ['name', 'inventory']
