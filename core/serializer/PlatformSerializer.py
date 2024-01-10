from rest_framework import serializers

from core.models.models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = 'id', 'name',

    def validate_name(self, value):
        if Platform.objects.filter(name=value).exists():
            raise serializers.ValidationError("Platform with this name already exists.")
        return value
