from email.policy import default
from rest_framework.routers import DefaultRouter
from .views import HealthInsuranceViewSet

router = DefaultRouter()

router.register('HealthInsurance', HealthInsuranceViewSet, basename='HealthInsurance')

urlpatterns = router.urls