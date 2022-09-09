from rest_framework import serializers
from .models import Purchase, PurchaseDetail


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseDetail
        fields = '__all__'
