from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .email import register_send_email
from .models import BlogUser, EmailVerifyRecord

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View


class Login(View):
    def get(self,request):
        return render(request,'login.html',{})
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, 'login.html', {'error_msg': "User hasn't been authenticated"})
        else:
            return render(request, 'login.html', {'error_msg': 'Wrong'})


class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


#Register in the Blog Web without authentication
class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        register_send_email(email)
        blog_user = BlogUser()
        blog_user.username = username
        blog_user.password = make_password(password)
        blog_user.email = email
        blog_user.is_active = False
        blog_user.save()
        return render(request, 'login.html')


class ActiveUser(View):
    def get(self, request, active_code):
        record_list = EmailVerifyRecord.objects.filter(code=active_code)
        if record_list:
            for record in record_list:
                email = record.email
                user = BlogUser.objects.get(email = email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'register_fail.html')


