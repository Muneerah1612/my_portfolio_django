from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Project


def homepage(request):
    ''' this function returns the specified response in the homepage page'''
    projects = Project.objects.all()
    return render(request,'projects/index.html',{'projects':projects})

def detail(request,project_id):
    ''' this function returns the details of each project '''
    project_detail = get_object_or_404(Project,pk=project_id)
    return render(request,'projects/detail.html', {'project':project_detail})


