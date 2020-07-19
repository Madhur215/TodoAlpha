from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Profile, TodoList


def Home(request):

    if not request.user.is_authenticated:
        print("Not logged In")
        return render(request, "main/index.html", {})
    else:
        return render(request, "main/Home.html", {})


def ToDoList(request):

    email = request.user.email
    user = Profile.objects.get(email=email)

    # print(user.todolist_set.all())

    for todo in user.todolist_set.all():
        print(todo.title)
        print(todo.description)
        print(todo.deadline)

    return render(request, "main/todo.html", {})

