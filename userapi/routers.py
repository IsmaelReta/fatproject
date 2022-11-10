from rest_framework.routers import DefaultRouter
from .views import UserFullViewSet, UserViewSet, TestFullViewSet

router = DefaultRouter()

router.register('f', UserViewSet, basename='users')
router.register('full', UserFullViewSet, basename='userfull')
router.register('testfull', TestFullViewSet, basename='testfull')

urlpatterns = router.urls
