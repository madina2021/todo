from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage (request):
    return HttpResponse("hello world")
    return render (request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def second(request):
    return HttpResponse("uraa test2")
    
def third(request):
    return HttpResponse("unforturnaly, but done")