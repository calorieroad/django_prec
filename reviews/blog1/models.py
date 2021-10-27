from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Article(models.Model):
    body = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.CharField(max_length=10)
