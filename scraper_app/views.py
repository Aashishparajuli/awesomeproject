from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    d={
        'names':['Aashish','shanks','kops']
    }
    return render(request,'scraper_app/index.html',d)

def aasis(request):
    return HttpResponse('Hi my name is aasis')