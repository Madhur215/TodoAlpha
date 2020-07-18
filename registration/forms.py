from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Profile
from django.forms import ModelForm


class SignUpForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email", "phone_number"]


class LoginForm(ModelForm):

    class Meta:
        model = Profile
        fields = ["email", "phone_number"]
