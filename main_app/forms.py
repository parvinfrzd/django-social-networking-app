from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['text', 'likes']

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password1=forms.CharField(required=True)
    password2=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
