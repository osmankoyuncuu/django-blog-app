from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "category",
            "category_id",
            "is_publish",
            "image",
            "created_date",
            "update_date",
        )


