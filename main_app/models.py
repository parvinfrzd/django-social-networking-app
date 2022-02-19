from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.TextField()
    like = models.ManyToManyField(User, blank=True, related_name='like') 
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike') 

    def __str__(self):
        return f"text: {self.text}"

class Comment(models.Model):
    text = models.TextField()
    like = models.ManyToManyField(User, blank=True, related_name='+') 
    dislike = models.ManyToManyField(User, blank=True, related_name='+') 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)