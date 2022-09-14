from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, SaleDetailViewSet

router = DefaultRouter()

router.register('', SaleViewSet, basename='')
router.register('', SaleDetailViewSet, basename='')


urlpatterns = router.urls