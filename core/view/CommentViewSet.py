# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets, status
# from rest_framework.response import Response
#
# from core.models.models import Comment, Prompt, User
# from core.serializer.CommentSerializer import CommentSerializer
# from core.serializer.PageNumberPagination import PageNumberPagination
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     pagination_class = PageNumberPagination
#     queryset = Comment.objects.all()
#     lookup_field = 'id'
#
#     def get_queryset(self):
#         prompt_id = self.request.query_params.get('promptId', None)
#         if prompt_id is not None:
#             return Comment.objects.filter(prompt_id=prompt_id)
#         return Comment.objects.none()
#
#     # def get_object(self):
#     #     comment_id = self.kwargs.get('id')
#     #     comment = get_object_or_404(Comment, id=comment_id)
#     #     return comment
#
#     def create(self, request, *args, **kwargs):
#         prompt_id = request.data.get('promptId')
#         user_id = request.data.get('userId')
#         content = request.data.get('content')
#
#         request.data['prompt'] = prompt_id
#         request.data['user'] = user_id
#         request.data['content'] = content
#
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# # https://blog.csdn.net/qq_37674086/article/details/107144807
