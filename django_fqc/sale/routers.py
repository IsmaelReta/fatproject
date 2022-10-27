from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, SaleDetailViewSet, SaleDetailWhatsAppViewSet

router = DefaultRouter()

router.register('', SaleViewSet, basename='Sales')
router.register(r'(?P<sale_id>[^/.]+)/details', SaleDetailViewSet, basename='details')
router.register(r'(?P<sale_id>[^/.]+)/detailswa', SaleDetailWhatsAppViewSet, basename='detailswa')


urlpatterns = router.urls
