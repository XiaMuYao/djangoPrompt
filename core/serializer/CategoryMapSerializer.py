from rest_framework import serializers

from core.models.models import CategoryMap


class CategoryMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMap
        fields = '__all__'
