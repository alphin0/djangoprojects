from django import forms
# from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','email','first_name','last_name','phone','address']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()