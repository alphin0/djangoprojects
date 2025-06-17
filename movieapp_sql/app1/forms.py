from django import forms
from .models import Movie

# class Movie_form(forms.Form):
#     movie_name=forms.CharField(max_length=100)
#     description=forms.CharField(widget=forms.Textarea)
#     director_name=forms.CharField()
#     language=forms.CharField()
#     year=forms.IntegerField()
#     image=forms.ImageField()

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'