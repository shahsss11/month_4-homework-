from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def quote1(request):
    return HttpResponse("Конфуций: 'Не важно, как медленно ты идёшь, пока не останавливаешься.'")

def quote2(request):
    return HttpResponse("Альберт Эйнштейн: 'Воображение важнее знания.'")

def quote3(request):
    return HttpResponse("Оскар Уайльд: 'Мы все рождаемся глупыми, но некоторые из нас решают остаться ими.'")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})