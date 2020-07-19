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

    return render(request, "main/todo.html", {"todoList": user.todolist_set.all()})


def removeToDo(request, title):

    user = Profile.objects.get(email=request.user.email)
    user.todolist_set.get(title=title).delete()
    return redirect("/todo")

