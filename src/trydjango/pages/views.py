from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")

def home_view_02(request,*args, **kwargs):
    my_context = {
        "myText": "This is about Us",
        "myNumber": 2023,
        "myList" : {1,2,3,4,5,6,7,8}
    }
    
    return render(request, "home.html", my_context)

def about_view(request,*args, **kwargs):
    my_context = {
        "myText": "This is about Us",
        "myNumber": 2023
    }
    return render(request, "about.html", my_context)
