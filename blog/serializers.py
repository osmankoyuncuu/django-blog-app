from rest_framework import serializers
from .models import Category, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CategorySerializer(serializers.ModelField):
    
    class Meta:
        model = Category
        fields = ['name']