from rest_framework import routers
from purchase.views import PurchaseViewSet, PurchaseDetailViewSet # noqa

router = routers.DefaultRouter()
router.register('purchases', PurchaseViewSet, basename='Purchases')
router.register('purchaseDetails', PurchaseDetailViewSet, basename='PurchaseDetails')

urlpatterns = router.urls
