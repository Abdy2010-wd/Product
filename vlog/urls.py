from django.urls import path
from .views import PostsListView, PostDetailView, CommentsListView, CommentDetailView

urlpatterns = [
    path("", PostsListView.as_view()),
    path("<int:id>/", PostDetailView.as_view()),
    path("<int:id>/comments/", CommentsListView.as_view()),
    path("<int:id>/comments/<int:pk>/", CommentDetailView.as_view()),
]

