from django.shortcuts import render
from django.contrib.auth.models import User


def SignUp():

    if User.is_authenticated:
        pass


