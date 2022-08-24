from django.contrib import admin
from .models import Person, HealthInsurance, Certificate, Tutor
# Register your models here.
admin.site.register(Person)
admin.site.register(HealthInsurance)
admin.site.register(Certificate)
admin.site.register(Tutor)
