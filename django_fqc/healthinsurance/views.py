from pyexpat import model
from django.shortcuts import render
from .models import HealthInsurance
from .serializers import HealthInsuranceSerializer
from rest_framework import viewsets

# Create your views here.

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = HealthInsuranceSerializer

    def get_queryset(self):
        insurance = HealthInsurance.objects.all()
        return insurance
        