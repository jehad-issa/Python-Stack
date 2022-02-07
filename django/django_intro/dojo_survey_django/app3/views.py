from django.shortcuts import render,redirect
def index(request):
    return render(request,"index.html")
        
def result(request):
    name = request.POST['name']
    location = request.POST['location']
    Language=request.POST['Language']
    Comment=request.POST['Comment']

    context={
        'name': name,
        'location': location,
        'Language': Language,
        'Comment': Comment
    }

    return render(request,"show.html",context)

def go_back(request):
    return redirect("/")