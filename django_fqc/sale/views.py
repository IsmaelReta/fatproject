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

    def get_queryset(self):
        sale_detail = SaleDetail.objects.all()
        return sale_detail
