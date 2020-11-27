from django.shortcuts import render
from django.http import HttpResponse as Response

def index(request):
    return Response("Rango says hey there partner!")