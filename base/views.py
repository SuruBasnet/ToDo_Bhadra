from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.

def home(request):
    objects = ToDo.objects.all()
    content = {'todos':objects}
    return render(request,'index.html',context=content)