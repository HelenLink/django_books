from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def menu(request):
    books = Book.objects.all()
    return render(request, 'books_app/Menu.html', {'books': books})


def one_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books_app/one_book.html', {'book': book})
