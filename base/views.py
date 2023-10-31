from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.

def home(request):
    objects = ToDo.objects.all()
    content = {'todos':objects} # Making the dictionary data to pass on template
    return render(request,'index.html',context=content)

def create(request):
    return render(request,'create.html')