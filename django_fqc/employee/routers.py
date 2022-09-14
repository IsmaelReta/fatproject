from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()

router.register('employee', EmployeeViewSet, basename='')

urlpatterns = router.urls