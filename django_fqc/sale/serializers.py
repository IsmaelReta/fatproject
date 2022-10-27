from dataclasses import fields
from rest_framework import serializers
from .models import Sale, SaleDetail
from product.serializers import ProductSerializerSale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        # fields = ['id', 'patient']
        fields = '__all__'


class SaleDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializerSale()

    class Meta:
        model = SaleDetail
        fields = ['id', 'amount', 'sale', 'product']
