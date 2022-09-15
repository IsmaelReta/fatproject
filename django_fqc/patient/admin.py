from django.contrib import admin

from .models import Patient, HealthInsurancePatient, Certificate, Tutor

# Register your models here.
admin.site.register(Patient)
admin.site.register(HealthInsurancePatient)
admin.site.register(Certificate)
admin.site.register(Tutor)
