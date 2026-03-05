from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def courses(request):
    return render(request, 'courses.html')

def vision(request):
    return render(request, 'vision.html' )

def machine(request):
    return render(request, 'machine.html' )

def contact(request):
    return render(request, 'contact.html' )





