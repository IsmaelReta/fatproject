from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, SaleDetailViewSet

router = DefaultRouter()

router.register('Sales', SaleViewSet, basename='Sales')
router.register('SaleDetails', SaleDetailViewSet, basename='SaleDetails')


urlpatterns = router.urls
