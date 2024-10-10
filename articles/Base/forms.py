from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['owner']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio']