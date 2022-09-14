from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TutorViewSet, CertificateViewSet, HealthInsuranceViewSet

router = DefaultRouter()

router.register('patients', PatientViewSet, basename='patients')
router.register('tutors', TutorViewSet, basename='tutors')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('healths', HealthInsuranceViewSet, basename='healths')

urlpatterns = router.urls
