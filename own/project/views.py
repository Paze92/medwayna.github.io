from django.shortcuts import render
from .models import Menu


def index(request):
    projects = Menu.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def hair(request):
    projects = Menu.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'hair.html', context)


def manic(request):
    projects = Menu.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'manic.html', context)
