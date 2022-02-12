from django.shortcuts import render,redirect
from .models import Ninja,Dojo
def index(request):
    context = {
    "all_the_Ninja":Ninja.objects.all(),
    "all_the_Dojo":Dojo.objects.all(),
    }
    return render( request,"index.html",context)

def process(request):
    new_Dojo = Dojo(name=request.POST['name'],city = request.POST['city'],state=request.POST['state'])
    new_Dojo.save()    
    
    return redirect ("/")

