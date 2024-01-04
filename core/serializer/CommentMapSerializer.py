from rest_framework import serializers

from core.models.models import CommentMap


class CommentMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMap
        fields = '__all__'
