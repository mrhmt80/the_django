from django import forms
from .models import UserPost

class UserPostForm(forms.Form):
   nama = forms.CharField(max_length = 100)
   picture = forms.ImageField()

class UserPostEditForm(forms.Form):
   nama = forms.CharField(
   	max_length = 100, 
    widget=forms.TextInput(attrs={
    	'class': 'special',
    	'id' : 'ini_User_edit_id',
    	})
   	)
   picture = forms.ImageField()