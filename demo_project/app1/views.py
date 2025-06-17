from django.shortcuts import render    #render is used to show a webpage

# Create your views here.
from django.http import HttpResponse

def home(request):
    context={'name':'Arun','Age':23}
    return render(request,'html1.html',context)

def first(request):
    return render(request,'html2.html')

def second(request):
    return render(request,'html3.html')

#return render(request,template_name,context)
#context - used to pass data from views to template files.
#context is a dictionary type variable containing keys and values.