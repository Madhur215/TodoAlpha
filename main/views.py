from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User


def Home(request):

    if not request.user.is_authenticated:
        print("Not logged In")
        return render(request, "main/index.html", {})
    else:
        return render(request, "main/Home.html", {})


# def index(response):
#     return render(response, "main/index.html", {})
#     # return HttpResponse("<h1>Hello</h1>")
