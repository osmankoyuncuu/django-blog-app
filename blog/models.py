from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    #author = User.name
    #user = User.email
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE )
    #favoriteUser = 
    #commentUser = 
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.title