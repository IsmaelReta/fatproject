# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Purchase, PurchaseDetail
# from .serializers import PurchaseSerializer, PurchaseDetailSerializer
#
# # Create your views here.
#
# #
# class PurchaseViewSet(viewsets.ModelViewSet):
#     serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         purchase = Purchase.objects.all()
#         return purchase
#
#
# class PurchaseDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = PurchaseDetailSerializer
#     queryset = PurchaseDetail.objects
#
#     def filter_queryset(self, queryset):
#         purchase_id = self.kwargs['purchase_id']
#         purchase_detail = PurchaseDetail.objects.filter(purchase=purchase_id)
#         return purchase_detail
