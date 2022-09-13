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
# from users.views import PersonViewSet, HealthInsuranceViewSet, CertificateViewSet, TutorViewSet
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
router.register('Employee', EmployeeViewSet, basename='Employee')
router.register('Patient', PatientViewSet, basename='Patient')
router.register('HealthInsurance', HealthInsuranceViewSet, basename='HealthInsurance')
router.register('Certificate', CertificateViewSet, basename='Certificate')
router.register('Tutor', TutorViewSet, basename='Tutor')
router.register('Purchase', PurchaseViewSet, basename='Purchase')
router.register('PurchaseDetail', PurchaseDetailViewSet, basename='PurchaseDetail')
router.register('Sale', SaleViewSet, basename='Sale')
router.register('SaleDetail', SaleDetailViewSet, basename='SaleDetail')


# router.register("person", PersonViewSet, basename="person")
# router.register("healthInsurance", HealthInsuranceViewSet, basename="healthInsurance")
# router.register("certificate", CertificateViewSet, basename="certificate")
# router.register("tutor", TutorViewSet, basename="Tutor")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', include(router.urls)),

]
