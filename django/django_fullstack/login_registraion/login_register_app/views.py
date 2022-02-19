from django.shortcuts import render,redirect

from .models import User
from django.contrib import messages
import bcrypt


def show_form(request):
    if 'first_name' in request.session:
        return redirect ("/success")
    return render(request,"show_form.html")


def register(request):
    errors = User.objects.register_validator(request.POST)
    request.session['coming_from']='REGISTER'


    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)     
        User.objects.create(first_name=request.POST['first_name'], password=pw_hash)
        User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash)
        messages.success(request, "User successfully create")
        if 'first_name' not in request.session:
            request.session['first_name']=request.POST['first_name']
        return redirect('/success')



def login(request):
    errors = User.objects.login_validator(request.POST)
    request.session['coming_from']='LOGIN'

    user = User.objects.filter(email=request.POST['email'])
    print(user)
    if (len(user)>0): 
        logged_user = User.objects.get(email=request.POST['email'])
    
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            messages.success(request,"user seccessfuly lonin")
            if 'first_name' not in request.session:
                request.session['first_name']=user[0].first_name
                print(request.session['first_name'])
            return redirect('/success')    
    else:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
    return redirect('/')


def success(request):
    if "first_name" not in request.session:
        return redirect("/")
    # context={
    #     "first_name":request.session['first_name']
    # }
    return render(request,"success.html")    

def clear(request):
    if 'first_name' in request.session:
        del request.session['first_name']
    return redirect('/')






    # User.objects.create(
    #     first_name=request.POST['first_name'],
    #     last_name=request.POST['last_name'],
    #     email=request.POST['email'],
    #     password=request.POST['password'],
    # )
    # return redirect('/')    