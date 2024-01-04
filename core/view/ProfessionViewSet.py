from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.models import Profession
from core.serializer.ProfessionSerializer import ProfessionSerializer


class ProfessionViewSet(APIView):
    def get(self, request):
        """
        获取所有 Profession
        :param request:
        :return:
        """
        profession = Profession.objects.all()
        serializer = ProfessionSerializer(profession, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        创建一个 Profession,如果重复了就返回失败
        :param request:
        :return:
        """
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        删除一个 Profession
        :param request:
        :return:
        """
        profession_id = request.data.get('id')
        profession = Profession.objects.get(id=profession_id)
        profession.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        """
        更新一个 Profession
        :param request:
        :return:
        """
        profession_id = request.data.get('id')
        profession = Profession.objects.get(id=profession_id)
        serializer = ProfessionSerializer(profession, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
