from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Category
from core.serializer.CategorySerializer import CategorySerializer


class CategoryViewSet(APIView):
    def get(self, request):
        """
        获取所有 Category
        :param request:
        :return:
        """
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        创建一个 Category,如果重复了就返回失败
        :param request:
        :return:
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        删除一个 Category
        :param request:
        :return:
        """
        category_id = request.query_params.get('id', None)
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        """
        更新一个 Category
        :param request:
        :return:
        """
        category_id = request.query_params.get('id', None)
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
