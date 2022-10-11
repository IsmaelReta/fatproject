from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
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


# class ConfirmOrder(viewsets.ModelViewSet):
#     @action(methods=['PUT'], detail=True, url_path='confirm-order')
#     def test(self, request, pk: int):
#         data = {'patient_id': int(request.data.get('patient_id'))}
#         print(data)
