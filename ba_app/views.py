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
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect ('/viewBookRend/' + str(book.id), context)


def addAuthor(request):
    Author.objects.create(name=request.POST["name"], notes=request.POST["notes"])
    return redirect ('/RenderAuthor')

def RenderAuthor(request):
    context={
        "Authors":Author.objects.all()
    }
    return render (request, 'author.html', context)

def viewAuthRend(request, author_id):
    context={
        "Books":Book.objects.all(),
        "Author":Author.objects.filter(id=author_id).get(),
    }
    return render (request, "viewAuthRend.html", context)

def viewAuthEdit(request):
    context= {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect ('/viewAuthRend/' + str(author.id), context)