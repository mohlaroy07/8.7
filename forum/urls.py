from django.urls import path
from .views import TopicListCreateView, CommentListCreateView, CommentReplyCreateView

urlpatterns = [
    path('topics/', TopicListCreateView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/reply/', CommentReplyCreateView.as_view()),
]