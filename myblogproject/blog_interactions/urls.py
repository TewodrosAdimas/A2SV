from django.urls import path
from .views import (
    BlogRatingCreateView,
    CommentListView,
    LikeCreateView,
    BlogRatingUpdateDeleteView,
    CommentUpdateDeleteView,
    LikeUpdateDeleteView,
)

urlpatterns = [
    path('ratings/', BlogRatingCreateView.as_view(), name='create_rating'),
    path('comments/', CommentListView.as_view(), name='list_comments'),
    path('likes/', LikeCreateView.as_view(), name='create_like'),
    
    # Update and delete blog rating
    path('ratings/<int:pk>/update/', BlogRatingUpdateDeleteView.as_view(), name='update_delete_rating'),

    # Update and delete comment
    path('comments/<int:pk>/update/', CommentUpdateDeleteView.as_view(), name='update_delete_comment'),

    # Update and delete like
    path('likes/<int:pk>/update/', LikeUpdateDeleteView.as_view(), name='update_delete_like'),
]
