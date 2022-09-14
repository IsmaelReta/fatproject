from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TutorViewSet, CertificateViewSet, HealthInsuranceViewSet

router = DefaultRouter()

router.register('patient',PatientViewSet ,basename='')
router.register('tutor',TutorViewSet ,basename='')
router.register('certificate',CertificateViewSet ,basename='')
router.register('health',HealthInsuranceViewSet ,basename='')

urlpatterns = router.urls