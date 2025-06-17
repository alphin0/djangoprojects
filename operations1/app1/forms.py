from django import forms
from django.forms import PasswordInput,RadioSelect, ChoiceField


class AdditionForm(forms.Form): #form structure definition
    number1=forms.IntegerField()
    number2=forms.IntegerField()

class FactorialForm(forms.Form):
    number1=forms.IntegerField()

class BmiForm(forms.Form): #form structure definition
    weight=forms.IntegerField()
    height=forms.IntegerField()

class SignupForm(forms.Form):
    username=forms.CharField(max_length=50,required=8)
    email=forms.CharField(max_length=50)
    password=forms.CharField(widget=PasswordInput)
    gender_choice=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gender_choice,widget=RadioSelect)
    role_choice=[('admin','Admin'),('student','Student')]
    role=forms.ChoiceField(choices=role_choice)


class CalorieForm(forms.Form):
    gender_choice = [('male', 'Male'), ('female', 'Female')]
    choose_gender=forms.ChoiceField(choices=gender_choice, widget=RadioSelect)
    weight = forms.IntegerField()
    height = forms.IntegerField()
    age=  forms.IntegerField()
    activity_level_choice = [('1.2', 'Sedentary(little/no exercise)'),
                             ('1.375', 'Lightly active(exercise 1-3 days/week)'),
                             ('1.55','moderate(exercise 4-5 days/week)'),
                             ('1.725','Very active(exercise 5-6 days/week)'),
                             ('1.9','extra active(very intensive activity')]
    activity_level = forms.ChoiceField(choices=activity_level_choice)

