from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Hi. This is about page')

def mainpage(request):
    return render (request, 'home.html')