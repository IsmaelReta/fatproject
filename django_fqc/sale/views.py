from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from .models import Sale, SaleDetail
from .serializers import SaleSerializer, SaleDetailSerializer, SaleDetailWhatsAppSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins

# Create your views here.


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer

    def get_queryset(self):
        sale = Sale.objects.all()
        return sale

#*Luego sacar List
class SaleDetailViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects


    def get_queryset(self):
        sale_id = self.kwargs["sale_id"]
        sale_detail = SaleDetail.objects.filter(sale=sale_id)
        p = self.request.user.patient.id
        sale = Sale.objects.filter(patient=p)
        print(sale)
        return sale_detail

    def create(self, request, *args, **kwargs):
        patient = self.request.user.patient
        patient_sales = Sale.objects.filter(patient=patient)
        sale_detail_data = request.data
        nsale = sale_detail_data['sale']
        nproduct = sale_detail_data['product']
        namount = sale_detail_data['amount']
        nprice = sale_detail_data['price']
        if nsale == patient_sales:
            pass
        else:
            pass
        new_sale_detail = SaleDetail.objects.create()
        return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)


    # def list(self, request, *args, **kwargs):
    #     patient = self.request.user.patient
    #     sale_detail_data = request.data
    #     patient_sales = Sale.objects.filter(patient=patient)
    #     print(patient_sales)
    #     a = self.get_object()
    #     b = a.sale
    #     print(b)
    #     return Response({'error': 'This data is not yours'}, status=status.HTTP_401_UNAUTHORIZED)




# class ConfirmOrder(viewsets.ModelViewSet):
#     @action(methods=['PUT'], detail=True, url_path='confirm-order')
#     def test(self, request, pk: int):
#         data = {'patient_id': int(request.data.get('patient_id'))}
#         print(data)


class SaleDetailWhatsAppViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SaleDetailWhatsAppSerializer

    def get_queryset(self):
        sale_id = self.kwargs["sale_id"]
        sale_detail = SaleDetail.objects.filter(sale=sale_id)
        return sale_detail
