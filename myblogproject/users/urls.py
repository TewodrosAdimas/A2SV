from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterViewSet, LoginViewSet, FollowViewSet, UpdateProfileView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('register', RegisterViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('users/update-profile/', UpdateProfileView.as_view(), name='update-profile'),  # Add this line
]
