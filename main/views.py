from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Profile, TodoList
from .forms import AddItemForm


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


def AddItem(request):

    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            date = form.cleaned_data.get('date')
            email = request.user.email
            user = Profile.objects.get(email=email)
            user.todolist_set.create(title=title, description=description, deadline=date)
            return redirect("/todo")
    else:
        form = AddItemForm()
    return render(request, "main/AddItem.html", {"form": form})


def UserProfile(request):
    email = request.user.email
    user = Profile.objects.get(email=email)

    return render(request, "main/profile.html", {"user": user})

