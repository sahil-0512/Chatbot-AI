from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Welcome to ThinkGPT. You're at the polls index.</h2>")

def page(request):
    return HttpResponse("<h1>Welcome Sahil</h1>")