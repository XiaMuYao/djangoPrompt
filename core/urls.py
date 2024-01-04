from xml.etree.ElementInclude import include

from django.urls import path
from rest_framework.routers import DefaultRouter

from core.view import CategoryViewSet
from core.view.CategoryViewSet import CategoryViewSet
from core.view.ProfessionViewSet import ProfessionViewSet
from core.view.PromptViewSet import PromptViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)


urlpatterns = [
    # path('prompts/', PromptList.as_view(), name='prompt-list'),
    # path('category/', CategoryList.as_view(), name='category-list'),
    path('category/', CategoryViewSet.as_view(), name='categoryAll'),
    path('profession/', ProfessionViewSet.as_view(), name='professionAll'),
    path('prompt/', PromptViewSet.as_view(), name='PromptView Search'),
    # path('category/', include(router.urls), name='category'),

    # path('profession/', ProfessionList.as_view(), name='Profession-list'),
]
