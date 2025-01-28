from django.urls import path
from .views import BlogListCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListCreateView.as_view(), name='blog_list_create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]

