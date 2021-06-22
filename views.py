from django.shortcuts import render
from app.models import Todo

# Create your views here.

def readdata(request):
    todo_list=Todo.objects.all()
    return render(request,"home.html",{'todo_list':todo_list})

def add_todo(request):
    newtask=Todo(task=request.POST['content'])
    newtask.save()