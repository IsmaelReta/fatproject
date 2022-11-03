from pyexpat import model
from django.shortcuts import render
from .models import HealthInsurance
from .serializers import HealthInsuranceSerializer
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

# Create your views here.


class HealthInsuranceViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = HealthInsuranceSerializer

    def get_queryset(self):
        insurance = HealthInsurance.objects.all()
        return insurance
