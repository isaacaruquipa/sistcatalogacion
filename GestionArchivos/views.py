from django.shortcuts import render

# django http request
from django.http import HttpResponse

def index(request):
    return HttpResponse("Sistema de gestion archivos")
