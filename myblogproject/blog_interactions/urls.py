from django.urls import path
from .views import BlogRatingCreateView, CommentListView, LikeCreateView

urlpatterns = [
    path('ratings/', BlogRatingCreateView.as_view(), name='create_rating'),
    path('comments/', CommentListView.as_view(), name='list_comments'),
    path('likes/', LikeCreateView.as_view(), name='create_like'),
]
