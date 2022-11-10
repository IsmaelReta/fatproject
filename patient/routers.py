from rest_framework.routers import DefaultRouter
from .views import (PatientViewSet, TutorViewSet, 
                    CertificateViewSet, HealthInsViewSet)

router = DefaultRouter()

router.register('patients', PatientViewSet, basename='patients')
router.register('tutors', TutorViewSet, basename='tutors')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('healthinsurances', HealthInsViewSet, basename='healthsinsurances')

urlpatterns = router.urls
