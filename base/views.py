from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo

# Create your views here.

def home(request):
    objects = ToDo.objects.all()
    content = {'todos':objects} # Making the dictionary data to pass on template
    return render(request,'index.html',context=content)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        ToDo.objects.create(name=name,description=description,status=status)

        return redirect('home')

    return render(request,'create.html')