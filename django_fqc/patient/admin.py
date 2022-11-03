from django.contrib import admin
from .models import Patient, HealthInsurancePatient, Certificate, Tutor
# Register your models here.


class TutorInLine(admin.TabularInline):
    model = Tutor
    extra = 0


class HealthInsurancePatientInLine(admin.TabularInline):
    model = HealthInsurancePatient
    extra = 0


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('patient', 'image')
    readonly_fields = ('image',)


class CertificateInLine(admin.TabularInline):
    model = Certificate
    extra = 0


class PatientAdmin(admin.ModelAdmin):
    inlines = [
        TutorInLine,
        HealthInsurancePatientInLine,
        # CertificateInLine,
    ]


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthInsurancePatient)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Tutor)
