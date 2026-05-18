from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Book


def quote1(request):
    return HttpResponse("Конфуций: 'Не важно, как медленно ты идёшь, пока не останавливаешься.'")

def quote2(request):
    return HttpResponse("Альберт Эйнштейн: 'Воображение важнее знания.'")

def quote3(request):
    return HttpResponse("Оскар Уайльд: 'Мы все рождаемся глупыми, но некоторые из нас решают остаться ими.'")


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'
    model = Book
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        books = self.model.objects.all()
        if search:
            books = books.filter(title__icontains=search)
        return books
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    model = Book

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj