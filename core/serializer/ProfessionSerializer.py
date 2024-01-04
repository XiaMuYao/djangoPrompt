from rest_framework import serializers

from core.models.models import Profession


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = 'id', 'name',

    def validate_name(self, value):
        if Profession.objects.filter(name=value).exists():
            raise serializers.ValidationError("Profession with this name already exists.")
        return value
