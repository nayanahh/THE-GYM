from django.shortcuts import render

def home(request):
    return render(request, 'index.html') # Make sure this matches your file name
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def classes(request):
    return render(request, 'classes.html')

def pricing(request):
    return render(request, 'pricing.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')