from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, CommentCreateView, CommentDetailView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comments-detail'),
]
