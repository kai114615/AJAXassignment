from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "assignment/index.html")

def travel(request):
    return render(request, "assignment/travel.html")

def todolist(request):
    return render(request, "assignment/todolist.html")
