from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User


def Home(response):

    # if User.is_authenticated:
    return render(response, "main/Home.html", {})
    # else:
    #     return render(response, "main/index.html")


def index(response):
    return render(response, "main/index.html", {})
    # return HttpResponse("<h1>Hello</h1>")
