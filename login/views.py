from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, world. You're at the polls index.</h2>")

def chat(request):
    return HttpResponse("<h1>Hello Sahil</h1>")