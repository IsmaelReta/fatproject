from django.shortcuts import render
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employee = Employee.objects.all()
        return employee
    
