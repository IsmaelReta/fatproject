from rest_framework import routers
from product.views import ProductViewSet # noqa

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = router.urls
