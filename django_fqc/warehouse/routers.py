from rest_framework import routers
from warehouse.views import WarehouseViewSet, InventoryViewSet # noqa

router = routers.DefaultRouter()
router.register('warehouse', WarehouseViewSet, basename='warehouse')
router.register('inventory', InventoryViewSet, basename='inventory')

urlpatterns = router.urls
