from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, SaleDetailViewSet

router = DefaultRouter()

router.register('Sale', SaleViewSet, basename='Sale')
router.register('SaleDetail', SaleDetailViewSet, basename='SaleDetail')


urlpatterns = router.urls
