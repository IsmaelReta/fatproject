from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    total_products = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id','name','description', 'price', 'total_p']
