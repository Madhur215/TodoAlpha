from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from main.models import Profile


def SignUp(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = SignUpForm()
        # return HttpResponse("<h1>Sign!</h1>")
        return render(request, "registration/signup.html", {"form": form})


def Login(request):

    if request.method == "POST":
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        check = Profile.objects.filter(email=email)
        if check:
            return redirect("/home")
        else:
            return redirect("/login")
    else:
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})