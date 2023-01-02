from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    is_publish = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post', default='post/blog.png')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    