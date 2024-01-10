from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Profession, Platform
from core.serializer.PlatformSerializer import PlatformSerializer
from core.serializer.ProfessionSerializer import ProfessionSerializer


class PlatformViewSet(APIView):
    def get(self, request):
        """
        获取所有 Platform
        :param request:
        :return:
        """
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        创建一个 Platform,如果重复了就返回失败
        :param request:
        :return:
        """
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        删除一个 Platform
        :param request:
        :return:
        """
        platform_id = request.query_params.get('id', None)
        platform = Profession.objects.get(id=platform_id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        """
        更新一个 Platform
        :param request:
        :return:
        """
        platform_id = request.query_params.get('id', None)
        platform = Profession.objects.get(id=platform_id)
        serializer = ProfessionSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
