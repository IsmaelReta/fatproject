from rest_framework.routers import DefaultRouter
from .views import (PatientViewSet, TutorViewSet, 
                    CertificateViewSet, HealthInsViewSet, 
                    PatientFullViewSet,)

router = DefaultRouter()

router.register('users', PatientViewSet, basename='patients')
router.register('tutors', TutorViewSet, basename='tutors')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('healthinsurances', HealthInsViewSet, basename='healthsinsurances')
router.register('full', PatientFullViewSet, basename='patientfull')

urlpatterns = router.urls
