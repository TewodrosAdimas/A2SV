from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
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


# Update and delete Blog Rating (Owner-only access)
class BlogRatingUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogRating.objects.all()
    serializer_class = BlogRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("You do not have permission to modify this rating.")
        super().check_object_permissions(request, obj)


# Update and delete Comment (Owner-only access)
class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("You do not have permission to modify this comment.")
        super().check_object_permissions(request, obj)


# Update and delete Like (Owner-only access)
class LikeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def check_object_permissions(self, request, obj):
        if obj.user != request.user:
            raise PermissionDenied("You do not have permission to modify this like.")
        super().check_object_permissions(request, obj)
