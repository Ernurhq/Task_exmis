from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),

    # Комментарии к конкретному посту (список и создание)
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),

    # Детальный доступ к комментарию (чтение, обновление, удаление)
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]
