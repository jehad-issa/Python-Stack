from urllib import request
from django.shortcuts import render, redirect
def index(request):
    if not "count" in request.session:
        request.session["count"] = 0
    else:    
        request.session["count"] += 1
    return render (request,'index.html')

def destroy(request):
    request.session.clear()				
    return redirect("/")    