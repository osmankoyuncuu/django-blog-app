from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post
from .serializers  import CategorySerializer, PostSerializer
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly
)

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        else:
            return request.user.is_staff  

class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


