from django.db.models.expressions import result
from django.shortcuts import render

# Create your views here.

def addition(request):

    if(request.method=='POST'):  #after form submission
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        # print(result)
        context={'result': result}
        return render(request,'addition.html',context)
    return render(request,'addition.html')


def fact(request):
        context={}
        if(request.method=='POST'):
            n1=request.POST['num3']
            num = int(n1)
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            context={'result':fact}
        return render(request,'factorial.html',context)

def bmi(request):
    context={}
    bmi = None
    category = ""
    if (request.method == 'POST'):
        weight=float(request.POST['weight'])
        height_cm=float(request.POST['height'])
        height_m=height_cm / 100
        bmi=round(weight / (height_m ** 2),2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        context = {'bmi': bmi, 'category':category}
    return render(request, 'bmi.html', context)
