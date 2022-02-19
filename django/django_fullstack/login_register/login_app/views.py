from urllib.request import Request
from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import bcrypt

def form_page(request):
    return render(request,"index1.html")


def register(request):

    errors = User.objects.registration_validator(request.POST)
    request.session['coming_from']='REGISTER'
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        print(request.POST['first_name'],
            request.POST['last_name'],
            request.POST['email'],
            request.POST['password'])
        password = request.POST['password']
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()      
        print(hash1)
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'])  
        messages.success(request, "User successfully created")
        return redirect('/success')


def login(request):
    errors = User.objects.login_validator(request.POST)
    request.session['coming_from']='LOGIN'

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        if(len(User.objects.filter(email=request.POST['email']))>0):
            messages.error(Request,"you are not register")
            if(Request.POST['password']!= User.objects.get(email=Request.POST['email']).password):
                messages.error(Request,"the password not correct")
                return redirect('/')
        messages.error(request,"you are not register")
        return redirect('/')
        
    else:
        
        messages.success(request, " successfully register or login")
        return redirect('/success')



def success(request):
    return render(request,"success.html")        






    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'])  
    return redirect('/')  
