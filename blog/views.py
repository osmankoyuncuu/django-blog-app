from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post
from .serializers  import CategorySerializer, PostSerializer

class PostMVS(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


