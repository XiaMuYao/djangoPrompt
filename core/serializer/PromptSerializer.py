from datetime import datetime

from rest_framework import serializers

from core.models.models import Prompt
from core.serializer.CategorySerializer import CategorySerializer
from core.serializer.PlatformSerializer import PlatformSerializer
from core.serializer.ProfessionSerializer import ProfessionSerializer
from core.serializer.TagSerializer import TagSerializer


class PromptSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    professions = ProfessionSerializer(read_only=True, many=True)
    platforms = PlatformSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=datetime.now())

    class Meta:
        model = Prompt
        fields = ['id', 'title', 'description',
                  'content', 'un_like', 'like',
                  'created_at', 'categories',
                  'professions', 'platforms', 'tags',"in_put","out_put"]
