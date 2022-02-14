from django.db import models

class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerField() 

    def __str__(self):
        return f"text: {self.text}"

class Comment(models.Model):
    text = models.TextField()
    likes = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)