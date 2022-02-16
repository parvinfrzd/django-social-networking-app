from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

COUNTRY = 0
CITY = 1

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    follows = models.ManyToManyField(
        "self", 
        related_name="followed_by", 
        symmetrical=False, 
        blank=True
    )

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('social:profile', kwargs={'pk': self.user.pk})



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        
        
class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerField() 

    def __str__(self):
        return f"text: {self.text}"

class Comment(models.Model):
    text = models.TextField()
    likes = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
