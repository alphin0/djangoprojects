"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Home.as_view(),name='home'),
    path('',views.Signup.as_view(),name='signup'),
    path('signin',views.Signin.as_view(),name='signin'),
    path('signout',views.SignOut.as_view(),name='signout'),
    path('verify_otp', views.OtpVerificationView.as_view(), name='verify_otp'),
    path('student', views.StudentHomeView.as_view(), name='student'),
    path('teacher', views.TeacherHomeView.as_view(), name='teacher'),
    path('ahome', views.AdminHomeView.as_view(), name='ahome'),
    path('accounts/',include('django.contrib.auth.urls'))

]
