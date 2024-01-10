from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Tag
from core.serializer.TagSerializer import TagSerializer


class TagViewSet(APIView):
    def get(self, request):
        """
        获取所有 Tag
        :param request:
        :return:
        """
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        创建一个 Tag,如果重复了就返回失败
        :param request:
        :return:
        """
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        删除一个 Tag
        :param request:
        :return:
        """
        tag_id = request.query_params.get('id', None)
        tag = Tag.objects.get(id=tag_id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        """
        更新一个 Profession
        :param request:
        :return:
        """
        tag_id = request.query_params.get('id', None)
        tag = Tag.objects.get(id=tag_id)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
