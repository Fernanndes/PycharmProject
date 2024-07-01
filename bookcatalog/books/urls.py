from django.urls import path
from .views import book_list, add_book

urlpatterns = [
    path('', book_list, name='book_list'),  # URL para a lista de livros
    path('add/', add_book, name='add_book'),  # URL para adicionar um novo livro
]
