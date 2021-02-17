from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    ''' this function returns the specified response in the homepage page'''
    return HttpResponse('Welcome 😄 ')

