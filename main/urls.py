from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home, name="home"),
    path("todo/", views.ToDoList, name="todo"),
    path("delete/<str:title>", views.removeToDo, name="remove"),
    path("addItem/", views.AddItem, name="addItem"),
]

