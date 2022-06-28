from django.shortcuts import render
from data.models import HealthInsurance, Product, Province, Address, User, Order, OrderDetail

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form1(request):
    return render(request, 'form1.html')