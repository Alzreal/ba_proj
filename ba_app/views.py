from django.shortcuts import redirect, render
from .models import *

def index(request):
    context={
        "Books" : Book.objects.all(),
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

def viewBookRend(request, book_id):
    context={
        "Book":Book.objects.filter(id=book_id).get(),
        "Authors":Author.objects.all()
    }
    return render (request, "viewBookRend.html", context)

def viewBookEdit(request):
    context= {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }
    book = Book.objects.get(id=request.POST['book'])
    author = Author.objects.get(id=request.POST['author'])
    author.books.add(book)
    return redirect ('/viewBookRend/<int:book_id>', context)