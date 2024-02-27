from django.shortcuts import render
from django.http import HttpResponse

from .models import Book


def fullBook(request):
    books = Book.objects.values("book_title", "ISBN", "id")
    return render(request, "book/books.html", {"book_list": books})


def getBookByID(request, book_id):
    try:
        context = {}
        book = Book.objects.get(id=book_id)
        context["book_list"] = [book]
        return render(request, "book/book.html", context)
    except:
        return HttpResponse(f"Error while getting a book with the id of {book_id}")


def getBookByName(request, book_name):
    context = {}
    try:
        book = Book.objects.filter(book_title__contains=book_name)
        context["book_list"] = book
        return render(request, "book/book.html", context)
    except:
        return HttpResponse(f"Error while getting a book with the name of {book_name}")