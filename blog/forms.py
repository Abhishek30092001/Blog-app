# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Comment
from django.contrib.auth.models import User
from .models import Comment
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
