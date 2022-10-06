from django.contrib import admin
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
# Register your models here.


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('patient', 'image')


admin.site.register(Patient)
admin.site.register(HealthInsurancePatient)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Tutor)
