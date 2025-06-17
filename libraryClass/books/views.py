from django.shortcuts import render, redirect
# Create your views here.
from books.forms import BookForms
from books.models import Books
from django.views import View


class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'home.html')


class Addbook(View):
    def get(self, request, *args, **kwargs):
        return render(request,'addbook.html')

    def post(self,request,*args,**kwargs):
        t = request.POST['t']
        a = request.POST['a']
        l = request.POST['l']
        p = request.POST['p']
        n = request.POST['n']
        i = request.FILES['i']
        b = Books.objects.create(title=t, author=a, language=l, pages=p, price=n, image=i)
        b.save()
        return render(request, 'addbook.html')

class Addbook1(View):
    def get(self, request, *args, **kwargs):
        form_instance = BookForms()
        return render(request, 'addbook1.html', {'form': form_instance})

    def post(self,request,*args,**kwargs):
        form_instance = BookForms(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')

class Viewbooks(View):
    def get(self,request,*args,**kwargs):
        b=Books.objects.all()
        print(b)
        return render(request,'viewbook.html',{'books':b})

class Details(View):
    def get(self,request,i,*args,**kwargs):
        b=Books.objects.get(id=i)
        return render(request,'details.html',{'books':b})

class Edit(View):
    def get(self,request,i,*args,**kwargs):
        b = Books.objects.get(id=i)
        form_instance = BookForms(instance=b)
        return render(request, 'edit.html', {'form': form_instance})

    def post(self,request,i,*args,**kwargs):
        b = Books.objects.get(id=i)
        form_instance = BookForms(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')


class Delete(View):
    def get(self,request,i,*args,**kwargs):
        b = Books.objects.get(id=i)  # or can use .delete()
        b.delete()
        return redirect('books:viewbook')

from django.db.models import Q

class Search(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'search.html')

    def post(self,request,*args,**kwargs):
        data = request.POST['q']
        b = Books.objects.filter(Q(title__icontains=data) | Q(author__contains=data) | Q(language__icontains=data))
        return render(request, 'search.html', {'books': b})