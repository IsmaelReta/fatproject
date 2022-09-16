from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientTutorViewSet, PatientCertificateViewSet, PatientHealthInsViewSet

router = DefaultRouter()

router.register('', PatientViewSet, basename='patients')
router.register(r'(?P<patient_id>[^/.]+)/tutors', PatientTutorViewSet, basename='tutors')
router.register(r'(?P<patient_id>[^/.]+)/certificates', PatientCertificateViewSet, basename='certificates')
router.register(r'(?P<patient_id>[^/.]+)/healthinsurances', PatientHealthInsViewSet, basename='healthsinsurances')

urlpatterns = router.urls
