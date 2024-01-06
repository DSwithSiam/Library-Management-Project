from django.db import models
from categories.models import Category
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'post')
    price = models.DecimalField(max_digits=5, decimal_places=1, null = True, blank = True)
    image = models.ImageField(upload_to='posts/', null= True, blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comment')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    creted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by - {self.name}"

