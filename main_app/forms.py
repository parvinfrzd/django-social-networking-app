from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password1=forms.CharField(required=True)
    confirm_password=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        
class PostForm(forms.ModelForm): 
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Write something here",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )    
    class Meta: 
        model = Post
        exclude = ("user", "created_at","likes","like","dislike")
        
class CommentForm(forms.ModelForm): 
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Write your comment here",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )
    class Meta: 
        model = Comment
        exclude = ("user", "created_at","post","likes","like","dislike")
