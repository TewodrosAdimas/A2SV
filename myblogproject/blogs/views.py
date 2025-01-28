from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission
from .models import Blog
from .serializers import BlogSerializer

# Custom permission to check if the logged-in user is the author of the post
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the owner can edit or delete their post
        return obj.author == request.user

# View to list and create blog posts
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for creating posts

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# View to retrieve a specific blog post
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# View to update a specific blog post
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only the owner can update the post

# View to delete a specific blog post
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only the owner can delete the post

