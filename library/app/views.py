from django.shortcuts import render, redirect
from .models import Book

def index(req):
    books = Book.objects.all()  
    return render(req, 'app/index.html', {'books' : books})

def post(req):
    title = req.POST.get('title')
    author = req.POST.get('author')
    genre = req.POST.get('genre')

    Book.objects.create(book_title=title, 
                        book_author=author, 
                        book_genre = genre)
    
    books = Book.objects.all()
    return render(req, 'app/index.html', {'books' : books})

def edit(req, id):
    books = Book.objects.get(id=id)
    return render(req, 'app/edit.html', {'books' : books})

def update(req, id):
    title = req.POST.get('title')
    author = req.POST.get('author')
    genre = req.POST.get('genre')

    books = Book.objects.get(id=id)
    books.book_title = title
    books.book_author = author
    books.book_genre = genre


    books.save()
    return redirect(index)

def delete(req, id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect(index) 

    