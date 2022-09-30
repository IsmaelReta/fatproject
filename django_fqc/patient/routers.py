from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientTutorViewSet, PatientCertificateViewSet, PatientHealthInsViewSet,\
    PatientUserViewSet, PatientFullViewSet, HIPost

router = DefaultRouter()

router.register('list', PatientViewSet, basename='patients')
router.register(r'(?P<patient_id>[^/.]+)/tutors', PatientTutorViewSet, basename='tutors')
router.register(r'(?P<patient_id>[^/.]+)/certificates', PatientCertificateViewSet, basename='certificates')
router.register(r'(?P<patient_id>[^/.]+)/healthinsurances', PatientHealthInsViewSet, basename='healthsinsurances')
router.register(r'(?P<patient_id>[^/.]+)/users', PatientUserViewSet, basename='users')
router.register('hipost', HIPost, basename='post_hi')
router.register('full', PatientFullViewSet, basename='patientfull')

urlpatterns = router.urls
