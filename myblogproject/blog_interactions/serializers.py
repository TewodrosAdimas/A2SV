from rest_framework import serializers
from .models import BlogRating, Comment, Like

class BlogRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogRating
        fields = ['id', 'rating_value', 'user', 'blog']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'blog', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'blog']
