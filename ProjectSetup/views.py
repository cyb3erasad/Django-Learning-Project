from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, This is home page")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')