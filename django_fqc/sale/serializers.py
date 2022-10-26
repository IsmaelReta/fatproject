from dataclasses import fields
from rest_framework import serializers
from .models import Sale, SaleDetail


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'patient']


class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ['id', 'amount', 'sale', 'product']
