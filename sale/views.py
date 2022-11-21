from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from .models import Sale, SaleDetail, Product
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
        return sale_detail

    def create(self, request, *args, **kwargs):
        patient = self.request.user.patient #*Patient request ID
        sale_detail_data = request.data

        new_sale_id = sale_detail_data['sale'] #*Data Sale
        s_sale = Sale.objects.filter(id=new_sale_id)
        new_product_id = sale_detail_data['product'] #*Data Sale
        new_amount = sale_detail_data['amount'] #*Data Sale
        new_price = sale_detail_data['price'] #*Data Sale

        new_sale = Sale.objects.get(id=new_sale_id)
        new_product = Product.objects.get(id=new_product_id)

        if s_sale.filter(patient=patient).exists():
            new_sale_detail = SaleDetail.objects.create(sale=new_sale, product=new_product, amount=new_amount, price=new_price)
            new_sale_detail.save()
            
            serializer = SaleDetailSerializer(new_sale_detail)

            return Response(serializer.data)

        else:
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
