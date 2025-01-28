from rest_framework import generics, permissions
from .models import BlogRating, Comment, Like
from .serializers import BlogRatingSerializer, CommentSerializer, LikeSerializer

# Create rating for a blog post
class BlogRatingCreateView(generics.CreateAPIView):
    queryset = BlogRating.objects.all()
    serializer_class = BlogRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

# List all comments for a blog post
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Create a like for a blog post
class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
