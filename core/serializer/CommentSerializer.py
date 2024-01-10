# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'content', 'created_at', 'prompt', 'user']
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user'] = UserSerializer(instance.user).data
#         return representation
