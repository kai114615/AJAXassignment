from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    return render(request, "assignment/index.html")

def travel(request):
    return render(request, "assignment/travel.html")

def todolist(request):
    # 讀取所有清單資料
    list = Todo.objects.all()
    print(list)
    return render(request, "assignment/todolist.html", locals())


def create(request):
    if request.method == 'POST':
        # print("測試")
        WhatYouDo = request.POST.get('inputWhatYouDo')
        # 新增資料
        Todo.objects.create(
            todo = WhatYouDo
        )
        return redirect('assignment:todolist')  # 完成新增後將重新刷新todolist頁面
