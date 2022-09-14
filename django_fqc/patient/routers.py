from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TutorViewSet, CertificateViewSet, HealthInsuranceViewSet

router = DefaultRouter()

router.register('patient', PatientViewSet, basename='patient')
router.register('tutor', TutorViewSet, basename='tutor')
router.register('certificate', CertificateViewSet, basename='certificate')
router.register('health', HealthInsuranceViewSet, basename='health')

urlpatterns = router.urls
