from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

# for creating a new user
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

# for creating/editing the articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['owner']

# for viewing/editing the user profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio']