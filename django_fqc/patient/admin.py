from django.contrib import admin

from .models import Patient, HealthInsurance, Certificate, Tutor

# Register your models here.
admin.site.register(Patient)
admin.site.register(HealthInsurance)
admin.site.register(Certificate)
admin.site.register(Tutor)
