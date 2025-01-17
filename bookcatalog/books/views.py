from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redireciona para a lista de livros após adicionar um novo livro
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})