from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Prompt, Category, Profession
from core.serializer.PromptSerializer import PromptSerializer


class PromptViewSet(APIView):
    # existing methods...

    def get(self, request):
        """
        Search for Prompts based on categoryID, professionID, and content
        """
        category_id = request.query_params.get('categoryID')
        profession_id = request.query_params.get('professionID')
        content = request.query_params.get('content')

        prompts = Prompt.objects.all()

        if category_id is not None:
            prompts = prompts.filter(categories__id=category_id)

        if profession_id is not None:
            prompts = prompts.filter(professions__id=profession_id)

        if content is not None:
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
                "profession_ids": [1, 2, 3]
            }
        """
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # 获取 category_id 和 profession_id
            category_ids = request.data.get('category_ids', [])
            profession_ids = request.data.get('profession_ids', [])

            # 创建 Prompt 实例
            prompt = serializer.instance

            # 在 CategoryMap 和 ProfessionMap 中创建新的实例
            for category_id in category_ids:
                category = Category.objects.get(id=category_id)
                prompt.categories.add(category)
            for profession_id in profession_ids:
                profession = Profession.objects.get(id=profession_id)
                prompt.professions.add(profession)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
