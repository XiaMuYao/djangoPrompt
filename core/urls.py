from django.urls import path

from core.view.CategoryViewSet import CategoryViewSet
from core.view.PlatformViewSet import PlatformViewSet
from core.view.ProfessionViewSet import ProfessionViewSet
from core.view.PromptViewSet import PromptViewSet
from core.view.TagViewSet import TagViewSet

# router = DefaultRouter()
# router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('category/', CategoryViewSet.as_view(), name='categoryAll'),
    path('profession/', ProfessionViewSet.as_view(), name='professionAll'),

    path('tag/', TagViewSet.as_view(), name='TagAll'),
    path('platform/', PlatformViewSet.as_view(), name='PlatformAll'),

    path('prompt/', PromptViewSet.as_view(), name='PromptView'),
]
