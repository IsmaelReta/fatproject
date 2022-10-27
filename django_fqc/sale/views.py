from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Sale, SaleDetail
from .serializers import SaleSerializer, SaleDetailSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins

# Create your views here.


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer

    def get_queryset(self):
        sale = Sale.objects.all()
        return sale


class SaleDetailViewSet(viewsets.ModelViewSet):
    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects

    def get_queryset(self):
        sale_id = self.kwargs["sale_id"]
        sale_detail = SaleDetail.objects.filter(sale=sale_id)
        return sale_detail

    def retrieve(self, request, *args, **kwargs):
        patient = self.request.user.patient
        sale_detail_data = request.data
        patient_sales = Sale.objects.filter(patient=patient)
        print(patient_sales)
        a = self.get_object()
        b = a.sale
        print(b)
        return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request, *args, **kwargs):
        patient = self.request.user.patient
        
        patient_sales = Sale.objects.filter(patient=patient)
        obj = self.get_object()
        obj_sale = obj.sale
        print(obj_sale)
        sale_detail_data = request.data
        new_sale_detail = SaleDetail.objects.create()
        return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)

# class ConfirmOrder(viewsets.ModelViewSet):
#     @action(methods=['PUT'], detail=True, url_path='confirm-order')
#     def test(self, request, pk: int):
#         data = {'patient_id': int(request.data.get('patient_id'))}
#         print(data)
