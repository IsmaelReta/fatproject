from dataclasses import fields
from rest_framework import serializers
from .models import Sale, SaleDetail


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model: SaleDetail
        fields = '__all__'
