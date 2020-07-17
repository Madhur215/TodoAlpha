from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home, name="home"),
    # path("", views.index, name="index"),
    # path("signup/", views.SignUp, name="SignUp"),
    # path("home/"),
    # path("register/"),
    # path("profile/"),
]

