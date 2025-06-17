from django.db.models.expressions import result
from django.shortcuts import render
from app1.forms import *


# Create your views here.
def addition(request):

    if request.method== 'POST':
        print(request.POST)
        return render(request,'addition.html')

    #get request
    form_instance=AdditionForm()  #empty from object
    return render(request,'addition.html',{'form':form_instance})


def fact(request):
    if request.method== 'POST':
        print(request.POST)
        return render(request,'factorial.html')

    form_fact=FactorialForm()
    return render(request,'factorial.html',{'form':form_fact})

def bmi(request):
    if request.method== 'POST':
        print(request.POST)
        return render(request,'bmi.html')

    form_bmi=BmiForm()
    return render(request,'bmi.html',{'form':form_bmi})

def signup(request):
    form_signup=SignupForm()
    return render(request,'signup.html',{'form':form_signup})


def calorie(request):
    if request.method== 'POST':#after the submission
        print(request.POST)

        #creating form object using data submitted by user
        form_calorie=CalorieForm(request.POST)

        #checks the validity of data using is_valid()
        if form_calorie.is_valid():

            #accessing the cleaned data after validation
            data=form_calorie.cleaned_data
            weight=data['weight']
            height=data['height']
            age=data['age']
            gender=data['choose_gender']
            activity_level=data['activity_level']
            print('weight:',weight,'height:',height,'age:',age,'gender:',gender,'activity_level:',activity_level)

        if data['choose_gender']=='male':
            bmr= 10 * weight + 6.25 * height - 5 * age + 5

        else:
            bmr=10 * weight + 6.25 * height - 5 * age - 161

        c = bmr * float(activity_level)
        print('Daily calorie',c)
        print('calorie_required',c)
        return render(request, 'calorie.html',{'form':form_calorie,'result':c})

    form_calorie=CalorieForm()
    return render(request,'calorie.html',{'form':form_calorie},)