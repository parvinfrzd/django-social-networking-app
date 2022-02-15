from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password1=forms.CharField(required=True)
    password2=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)