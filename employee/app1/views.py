from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def home(request):
    e=Employee.objects.all()
    return render(request,'home.html',{'employee':e})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'add_details.html', {'form': form})

def edit(request,i):
    e=Employee.objects.get(id=i)
    if (request.method == 'POST'):
        form_instance = EmployeeForm(request.POST, request.FILES,instance=e)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('home')

    form_instance=EmployeeForm(instance=e)
    return render(request,'edit.html',{'form':form_instance})


def details(request,i):
    e=Employee.objects.get(id=i)
    return render(request,'details.html',{'details':e})

def delete(request,i):
    e=Employee.objects.get(id=i)
    e.delete()
    return redirect('home')
