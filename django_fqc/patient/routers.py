from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TutorViewSet, PatientCertificateViewSet, PatientHealthInsViewSet,\
    PatientUserViewSet, PatientFullViewSet, HIPost

router = DefaultRouter()

router.register('list', PatientViewSet, basename='patients')
router.register('tutors', TutorViewSet, basename='tutors')
router.register('certificates', PatientCertificateViewSet, basename='certificates')
router.register(r'(?P<patient_id>[^/.]+)/healthinsurances', PatientHealthInsViewSet, basename='healthsinsurances')
router.register('users', PatientUserViewSet, basename='users')
router.register('hipost', HIPost, basename='post_hi')
router.register('full', PatientFullViewSet, basename='patientfull')

urlpatterns = router.urls
