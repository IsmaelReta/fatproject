from email.policy import default
from rest_framework.routers import DefaultRouter
from .views import HealthInsuranceViewSet

router = DefaultRouter()

router.register('', HealthInsuranceViewSet, basename='healthinsurances')

urlpatterns = router.urls
