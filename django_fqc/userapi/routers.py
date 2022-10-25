from rest_framework.routers import DefaultRouter
from .views import UserFullViewSet, UserViewSet, UserFullSerializer

router = DefaultRouter()

router.register('f', UserViewSet, basename='users')
router.register('full', UserFullViewSet, basename='userfull')

urlpatterns = router.urls
