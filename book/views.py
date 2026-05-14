from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F
from .models import Book


def quote1(request):
    return HttpResponse("Конфуций: 'Не важно, как медленно ты идёшь, пока не останавливаешься.'")

def quote2(request):
    return HttpResponse("Альберт Эйнштейн: 'Воображение важнее знания.'")

def quote3(request):
    return HttpResponse("Оскар Уайльд: 'Мы все рождаемся глупыми, но некоторые из нас решают остаться ими.'")


def book_list(request):
    search = request.GET.get('search', '')
    books = Book.objects.all()
    if search:
        books = books.filter(title__icontains=search)
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj,'search': search})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    book.views += 1
    book.save()
    return render(request, 'books/book_detail.html', {'book': book})
