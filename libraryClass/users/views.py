from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login ,logout
from users.forms import LoginForm
from users.forms import SignupForm
from django.core.mail import send_mail
from django.contrib import messages
from users.models import CustomUser


# Create your views here.

class Signup(View):
    def post(self,request):
        form_instance =SignupForm(request.POST)
        if form_instance.is_valid():
            # user=form_instance.save(commit=False) #here user represents model_instance created
            # user.set_password(form_instance.cleaned_data['password']) #changes the plaintext password
                                                                        #format into encryted format using django
                                                                        #SHA algorithom
            user = form_instance.save(commit=False)
            user.is_active = False
            user.save()
            user.generate_otp()
            send_mail(
                "Django_auth OTP",
                user.otp,
                "mpalphin@gmail.com",
                [user.email],
                fail_silently=False,
            )
            # user.save()
            return redirect('books:viewbook')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'register.html',{'form':form_instance})

class Signin(View):
    def post(self, request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                u = request.user
                print(u)
                return redirect('books:home')
            else:
                print('invalid username or password')
                return redirect('users:login')

    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

class OtpVerificationView(View):
    def post(self,request):
        otp = request.POST['otp']
        print(otp)
        otp = request.POST.get('otp')
        try:
            u = CustomUser.objects.get(otp=otp)
            u.is_active = True
            u.is_verified = True
            u.otp = None
            u.save()
            return redirect('signup')
        except:
            messages.error(request,'Invalid OTP')
            return redirect('verify_otp')


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('login')
