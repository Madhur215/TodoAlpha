from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "password"]


class LoginForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["email", "password"]

