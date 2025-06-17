from django.shortcuts import render , redirect
from app1.forms import Movie_form
from app1.models import Movie

# Create your views here.
def home(request):
    m = Movie.objects.all()
    return render(request,'home.html',{'Movie':m})


def addmovie(request):
    if (request.method=='POST'):
        print(request.POST)
        form_instance=Movie_form(request.POST,request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            movie_name=data['movie_name']
            description=data['description']
            director_name=data['director_name']
            language=data['language']
            year=data['year']
            image=data['image']
            m=Movie.objects.create(movie_name=movie_name,description=description,director_name=director_name,language=language,year=year,image=image)
            m.save()
        return redirect('home')

    form_instance = Movie_form()
    return render(request, 'addmovie.html',{'form':form_instance})

def details(request,i):
    m=Movie.objects.get(id=i)
    return render(request,'details.html',{'movies':m})

def edit(request,i):
    m = Movie.objects.get(id=i)
    if (request.method == 'POST'):
        form_instance = Movie_form(request.POST, request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('home')

    form_instance=Movie_form(instance=m)
    return render(request,'edit.html',{'form':form_instance})

def delete(request,i):
    m = Movie.objects.get(id=i) #or can use .delete()
    m.delete()
    return redirect('home')