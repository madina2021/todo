from django.shortcuts import render, HttpResponse

def homepage (request):
    return HttpResponse("hello world")
    return render (request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("uraa test2")
    
def third(request):
    return HttpResponse("unforturnaly, but done")