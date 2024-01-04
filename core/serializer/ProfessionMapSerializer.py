from rest_framework import serializers

from core.models.models import ProfessionMap


class ProfessionMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionMap
        fields = '__all__'
