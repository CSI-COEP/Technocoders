from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from datetime import date


def index(request):
    return render(request, 'index.html')

def contractor_signup(request):
    error=""
    if request.method=='POST':
        f = request.POST['fname'];
        l = request.POST['lname'];
        i = request.FILES['image'];
        p = request.POST['pwd'];
        e = request.POST['email'];
        con = request.POST['contact'];
        comp = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f,last_name=l, username=e, password=p)
            ContractorUser.objects.create(user=user, mobile=con, image=i, company=comp, type="contractor")
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {'error' :error}
    return render(request, 'cregister.html',d)

def contractor_login(request):
    error = ""
    if request.method == "POST":
       u = request.POST['uname']
       p = request.POST['pwd']
       user = authenticate(username=u, password=p)
       if user:
           try:
               user1 = ContractorUser.objects.get(user=user)
               if user1.type == "contractor":
                   login(request, user)
                   error = "no"
               else:
                   error = "yes"
           except:
               error = "yes"
       else:
           error = "yes"
    d = {'error': error}
    return render(request, 'clogin.html', d)

def government_signup(request):
    error=""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        state = request.POST['state']
        try:
            user = User.objects.create_user(first_name=f,last_name=l, username=e, password=p)
            GovernmentUser.objects.create(user=user, mobile=con, image=i, state=state, type ="government")
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {'error' :error}
    return render(request, 'gregister.html',d)

def government_login(request):
    error = ""
    if request.method == "POST":
       u = request.POST['uname']
       p = request.POST['pwd']
       user = authenticate(username=u, password=p)
       if user:
           try:
               user1 = GovernmentUser.objects.get(user=user)
               if user1.type == "government":
                   login(request, user)
                   error = "no"
               else:
                   error = "yes"
           except:
               error = "yes"
       else:
           error = "yes"
    d = {'error': error}
    return render(request, 'glogin.html', d)

def contractor_home(request):
    if not request.user.is_authenticated:
        return redirect('contractor_login')
    user = request.user
    contractor = ContractorUser.objects.get(user=user)
    d = {'contractor': contractor}
    return render(request, 'chome.html', d)


def government_home(request):
    if not request.user.is_authenticated:
        return redirect('government_login')
    user = request.user
    government = GovernmentUser.objects.get(user=user)
    d = {'government': government}
    return render(request, 'ghome.html', d)


def Logout(request):
    logout(request)
    return redirect('index')
