from django.shortcuts import render
from rest_framework import viewsets
from .models import Purchase, PurchaseDetail
from .serializers import PurchaseSerializer, PurchaseDetailSerializer

# Create your views here.


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        purchase = Purchase.objects.all()
        return purchase


class PurchaseDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseDetailSerializer

    def get_queryset(self):
        purchase_detail = PurchaseDetail.objects.all()
        return purchase_detail
