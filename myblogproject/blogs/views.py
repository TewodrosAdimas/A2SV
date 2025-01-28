from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer

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
