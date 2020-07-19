from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home, name="home"),
    path("todo/", views.ToDoList, name="todo"),
    # path("signup/", views.SignUp, name="SignUp"),
    # path("home/"),
    # path("register/"),
    # path("profile/"),
]

