from django.db import models
from django.contrib.auth import get_user_model
from blogs.models import Blog  # Import the Blog model

# Get the user model to associate interactions with users
User = get_user_model()

class BlogRating(models.Model):
    rating_value = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating value from 1 to 5
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating of {self.rating_value} for {self.blog.title} by {self.user.username}"

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on {self.blog.title}"
