from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'opinion.html')

def mundo(request):
    return render(request, 'mundo.html')

def contacto(request):
    return render(request, 'contacto.html')