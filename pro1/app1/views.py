from django.shortcuts import render

from django.http import HttpResponse

#Home view
def home(request):
    return HttpResponse('Django')

def index(request):
    return HttpResponse('Hello Django')