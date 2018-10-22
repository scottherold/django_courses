from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Description

# Create your views here.

def index(request):
    return render(request, 'courses/index.html', {"courses": Course.objects.all() })

def destroy(request, number):
    if request.method == "POST":
        course = Course.objects.get(id=number)
        course.delete()
        return redirect('/courses')
    else:
        return render(request, 'courses/destroy.html', {"course": Course.objects.get(id=number) })

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses/')
    else:
        course = Course.objects.create(name=request.POST['name'])
        course.save()
        desc = Description.objects.create(desc=request.POST['desc'], course=course)
        desc.save()
        print(desc.__dict__)
        return redirect('/courses/')