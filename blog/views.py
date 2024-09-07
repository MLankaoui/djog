from django.shortcuts import render
from django.http import HttpResponse


# the index page
def index(request):
    return HttpResponse("<h1> Home page </h1>")