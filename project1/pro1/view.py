from django.http import HttpResponse

def sample(request):
    return HttpResponse("helloworld")

def sample1(request):
    return HttpResponse("hello guys how are you")

def index(request):
    return HttpResponse("index function")

def index2(request):
    return HttpResponse("hii guys good evening")

def sample3(request):
    return HttpResponse("<h1>this h1 header tag and sample3 function response</h1>")