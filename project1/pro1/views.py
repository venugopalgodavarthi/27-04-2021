from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("this is hello function inside the views.py file") 

def hello1(req):
    return HttpResponse("this is hello1 function inside the views.py file we can given any name in function argument")

def imgs(request):
    return HttpResponse(" <marquee> hii hello world  gor corona </marquee>", status = 200 )

