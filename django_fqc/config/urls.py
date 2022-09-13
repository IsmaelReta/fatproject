"""django_fqc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import ProductViewSet
from warehouse.views import WarehouseViewSet, InventoryViewSet
from employee.views import EmployeeViewSet
from patient.views import PatientViewSet, HealthInsuranceViewSet, CertificateViewSet, TutorViewSet
from purchase.views import PurchaseViewSet, PurchaseDetailViewSet
from sale.views import SaleViewSet, SaleDetailViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('warehouse', WarehouseViewSet, basename='warehouse')
router.register('inventory', InventoryViewSet, basename='inventory')
router.register('employee', EmployeeViewSet, basename='Employee')
router.register('patient', PatientViewSet, basename='Patient')
router.register('healthInsurance', HealthInsuranceViewSet, basename='HealthInsurance')
router.register('certificate', CertificateViewSet, basename='Certificate')
router.register('tutor', TutorViewSet, basename='Tutor')
router.register('purchase', PurchaseViewSet, basename='Purchase')
router.register('purchaseDetail', PurchaseDetailViewSet, basename='PurchaseDetail')
router.register('sale', SaleViewSet, basename='Sale')
router.register('saleDetail', SaleDetailViewSet, basename='SaleDetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
