from django.shortcuts import redirect, render
from .models import *

def index(request):
    context={
        "Books" : Book.objects.all(),
        "Authors" : Author.objects.all()
    }
    return render (request, "index.html", context)

def addBook(request):
    Book.objects.create(title=request.POST["title"], description = request.POST["description"])
    return redirect ("/")

def RenderAuthor(request):
    context={
        "Authors":Author.objects.all()
    }
    return render (request, 'author.html', context)

def addAuthor(request):
    Author.objects.create(name=request.POST["name"], notes=request.POST["notes"])
    return redirect ('/RenderAuthor')