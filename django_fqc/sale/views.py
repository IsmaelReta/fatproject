from django.shortcuts import render
from rest_framework import viewsets

from .models import Sale, SaleDetail
from .serializers import SaleSerializer, SaleDetailSerializer
# Create your views here.


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer

    def get_queryset(self):
        sale = Sale.objects.all()
        return sale


class SaleDetailViewSet(viewsets.ModelViewSet):
    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects

    def filter_queryset(self, queryset):
        sale_id = self.kwargs["sale_id"]
        sale_detail = SaleDetail.objects.filter(sale=sale_id)
        return sale_detail



