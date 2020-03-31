from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter the password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
