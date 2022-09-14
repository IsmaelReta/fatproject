from rest_framework import routers
from purchase.views import PurchaseViewSet, PurchaseDetailViewSet # noqa

router = routers.DefaultRouter()
router.register('purchase', PurchaseViewSet, basename='Purchase')
router.register('purchaseDetail', PurchaseDetailViewSet, basename='PurchaseDetail')

urlpatterns = router.urls
