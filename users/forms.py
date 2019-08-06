from django import forms
from django.forms import ModelForm
from .models import Users
  
class UsersForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Users
        fields = 'user_id','name'

