from django.shortcuts import render , redirect
from app1.forms import Movie_form
from app1.models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView

# Create your views here.
# def home(request):
#     m = Movie.objects.all()
#     return render(request,'home.html',{'Movie':m})

class Home(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'Movie'

# def addmovie(request):
#     if (request.method=='POST'):
#         print(request.POST)
#         form_instance=Movie_form(request.POST,request.FILES)
#         if form_instance.is_valid():
#             data=form_instance.cleaned_data
#             print(data)
#             movie_name=data['movie_name']
#             description=data['description']
#             director_name=data['director_name']
#             language=data['language']
#             year=data['year']
#             image=data['image']
#             m=Movie.objects.create(movie_name=movie_name,description=description,director_name=director_name,language=language,year=year,image=image)
#             m.save()
#         return redirect('home')
#
#     form_instance = Movie_form()
#     return render(request, 'addmovie.html',{'form':form_instance})
from django.views.generic import CreateView
class AddmovieView(CreateView):
    form_class = Movie_form
    template_name = 'addmovie.html'
    model = Movie
    success_url = reverse_lazy('home')


# def details(request,i):
#     m=Movie.objects.get(id=i)
#     return render(request,'details.html',{'movies':m})
from django.views.generic import DetailView
class Detail(DetailView):
    model = Movie
    template_name = 'details.html'
    context_object_name = 'movies'


# def edit(request,i):
#     m = Movie.objects.get(id=i)
#     if (request.method == 'POST'):
#         form_instance = Movie_form(request.POST, request.FILES,instance=m)
#         if form_instance.is_valid():
#             form_instance.save()
#         return redirect('home')
#
#     form_instance=Movie_form(instance=m)
#     return render(request,'edit.html',{'form':form_instance})
from django.views.generic import UpdateView
class Edit(UpdateView):
    model = Movie
    form_class = Movie_form
    template_name = 'edit.html'
    success_url = reverse_lazy('home')

# def delete(request,i):
#     m = Movie.objects.get(id=i) #or can use .delete()
#     m.delete()
#     return redirect('home')

from django.views.generic import DeleteView
class Delete(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

