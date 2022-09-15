from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientTutorViewSet, CertificateViewSet, HealthInsuranceViewSet

router = DefaultRouter()

router.register('', PatientViewSet, basename='patients')
router.register(r'(?P<patient_id>[^/.]+)/tutors', PatientTutorViewSet, basename='tutors')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('healths', HealthInsuranceViewSet, basename='healthsinsurances')

urlpatterns = router.urls
