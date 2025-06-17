
from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm
from django.contrib.auth import authenticate , login ,logout
from django.core.mail import send_mail
from django.contrib import messages
from app1.models import CustomUser


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
            return redirect('verify_otp')
        return render(request, 'signup.html',{'form': form_instance})

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
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('ahome')
            elif user and user.role=='student':
                login(request, user)
                return redirect('student')
            elif user and user.role == 'teacher':
                login(request, user)
                return redirect('teacher')
            else:
                print('invalid username or password')


    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

class SignOut(View):
    def get(self,request):
        logout(request)
        return redirect('signin')

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

    def get(self,request):
        return render(request,'verify_otp.html')


class StudentHomeView(View):
    def get(self,request):
        return render(request,'student.html')

class TeacherHomeView(View):
    def get(self,request):
        return render(request,'teacher.html')

class AdminHomeView(View):
    def get(self,request):
        return render(request,'admin.html')

