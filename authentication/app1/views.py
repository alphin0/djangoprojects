
from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm
from django.contrib.auth import authenticate , login ,logout




class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Signup(View):
    def post(self,request):
        form_instance =SignupForm(request.POST)
        if form_instance.is_valid():
        #     user=form_instance.save(commit=False) #here user represents model_instance created
        #     user.set_password(form_instance.cleaned_data['password']) #changes the plaintext password
        #                                                                 #format into encryted format using django
        #                                                                 #SHA algorithom
        #     user.save()
            form_instance.save()
            return redirect('home')
        return render(request, 'home.html')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})



class Signin(View):
    def post(self, request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                print('invalid username or password')
                return redirect('login')

    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

class SignOut(View):
    def get(self,request):
        logout(request)
        return redirect('login')

