from rest_framework import routers
from warehouse.views import WarehouseViewSet, InventoryViewSet # noqa

router = routers.DefaultRouter()
router.register('', WarehouseViewSet, basename='warehouses')
router.register('inventories', InventoryViewSet, basename='inventories')

urlpatterns = router.urls
