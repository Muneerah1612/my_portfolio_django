from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def homepage(request):
    ''' this function returns the specified response in the homepage page'''
    projects = Project.objects
    return render(request,'projects/index.html',{'projects':projects})

