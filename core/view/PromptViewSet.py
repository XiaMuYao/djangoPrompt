import django.utils.timezone as timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Prompt, Category, Profession, Platform, Tag
from core.serializer.PromptSerializer import PromptSerializer


class PromptViewSet(APIView):

    def get(self, request):
        """
        Search for Prompts based on categoryID, professionID, tagId,platformId,and content
        """
        category_id = request.query_params.get('categoryId')
        profession_id = request.query_params.get('professionId')

        tag_id = request.query_params.get('tagId')
        platform_id = request.query_params.get('platformId')

        content = request.query_params.get('content')

        prompts = Prompt.objects.all()

        if category_id:
            prompts = prompts.filter(categories__id=category_id)

        if profession_id:
            prompts = prompts.filter(professions__id=profession_id)

        if tag_id:
            prompts = prompts.filter(tags__id=tag_id)

        if platform_id:
            prompts = prompts.filter(platforms__id=platform_id)

        if content:
            prompts = prompts.filter(content__icontains=content)

        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        创建一个 Prompt，并处理一对多的关系
            {
                "title": "Your title",
                "description": "Your description",
                "content": "Your content",
                "category_ids": [1, 2, 3],
                "profession_ids": [1, 2, 3],
                "tag_ids": [1, 2, 3],
                "platform_ids": [1, 2, 3],
            }
        """
        serializer = PromptSerializer(data=request.data)
        serializer.created_at = timezone.now()
        if serializer.is_valid():
            serializer.save()

            # 获取 category_id 和 profession_id
            category_ids = request.data.get('category_ids', [])
            profession_ids = request.data.get('profession_ids', [])
            tag_ids = request.data.get('tag_ids', [])
            platform_ids = request.data.get('platform_ids', [])

            # 创建 Prompt 实例
            prompt = serializer.instance

            # 在 Category Profession Tag Platform 的对应表中创建新的实例
            for category_id in category_ids:
                category = Category.objects.get(id=category_id)
                prompt.categories.add(category)

            for profession_id in profession_ids:
                profession = Profession.objects.get(id=profession_id)
                prompt.professions.add(profession)

            for tag_id in tag_ids:
                tag = Tag.objects.get(id=tag_id)
                prompt.tags.add(tag)

            for platform_id in platform_ids:
                platform = Platform.objects.get(id=platform_id)
                prompt.platforms.add(platform)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        prompt_id = request.query_params.get('id', None)
        prompt = Prompt.objects.get(id=prompt_id)
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
