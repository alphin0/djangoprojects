from django import forms

# from library.books.models import Books

from books.models import Books
# class BookForms(forms.Form): #form structure definition
#     title = forms.CharField()
#     author = forms.CharField()
#     language = forms.CharField()
#     pages= forms.IntegerField()
#     price= forms.IntegerField()
#     image = forms.ImageField()


class BookForms(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"