from django.shortcuts import render, redirect
# Create your views here.
from books.forms import BookForms
from books.models import Books


def home(request):
    return render(request,'home.html')

def addbook(request):
    # print(request.POST)
    # print(request.FILES)
    if request.method=='POST':
        t = request.POST['t']
        a = request.POST['a']
        l = request.POST['l']
        p = request.POST['p']
        n = request.POST['n']
        i = request.FILES['i']
        b=Books.objects.create(title=t,author=a,language=l,pages=p,price=n,image=i)
        b.save()
        return render(request, 'addbook.html')
    return render(request,'addbook.html')


def addbook1(request):
    if (request.method=='POST'):
        # print(request.POST)
        # print(request.FILES)
        form_instance = BookForms(request.POST,request.FILES)
        if form_instance.is_valid():
            # b=Books.objects.create(title=form_instance.cleaned_data['title'],
            #                        author=form_instance.cleaned_data['author'],
            #                        language=form_instance.cleaned_data['language'],
            #                        pages=form_instance.cleaned_data['pages'],
            #                        price=form_instance.cleaned_data['price'],
            #                        image=form_instance.cleaned_data['image'])

            # b.save()
            form_instance.save()
        return redirect('books:viewbook')

    form_instance = BookForms()
    return render(request, 'addbook1.html',{'form':form_instance})


def viewbook(request):
    b=Books.objects.all()
    print(b)
    return render(request,'viewbook.html',{'books':b})

def details(request,i):
    b=Books.objects.get(id=i)
    return render(request,'details.html',{'books':b})

def edit(request,i):
    b = Books.objects.get(id=i)
    if (request.method == 'POST'):
        form_instance = BookForms(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')

    form_instance=BookForms(instance=b)
    return render(request,'edit.html',{'form':form_instance})

def delete(request,i):
    b = Books.objects.get(id=i) #or can use .delete()
    b.delete()
    return redirect('books:viewbook')

from django.db.models import Q
def search(request):
    if (request.method=="POST"):
        data=request.POST['q']
        print(data)
        b=Books.objects.filter(Q(title__icontains=data) | Q(author__contains=data) | Q(language__icontains=data))
        #Q object - to use logical and/or/not syntax in ORM squeries
        #django lookups syntax= (fieldname__lookups )eg:(age__gt==data),age__lt,(title__icontains=data)#usees for case sensitive
        print(b)
        return render(request,'search.html',{'books':b})
    return render(request,'search.html')