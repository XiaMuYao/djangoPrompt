from rest_framework import serializers

from core.models.models import Prompt
from core.serializer.CategorySerializer import CategorySerializer
from core.serializer.CommentSerializer import CommentSerializer
from core.serializer.ProfessionSerializer import ProfessionSerializer


class PromptSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    professions = ProfessionSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Prompt
        fields = ['id', 'title', 'description',
                  'content', 'un_like', 'like',
                  'created_at', 'comments', 'categories',
                  'professions']
