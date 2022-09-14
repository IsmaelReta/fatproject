from rest_framework import serializers
from .models import HealthInsurance

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
        fields = '__all__'
