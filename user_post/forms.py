from django import forms
from .models import UserPost

class UserPostForm(forms.Form):
   nama = forms.CharField(max_length = 100)
   picture = forms.ImageField()