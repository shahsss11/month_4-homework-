from django.shortcuts import render
from django.http import HttpResponse

def quote1(request):
    return HttpResponse("Конфуций: 'Не важно, как медленно ты идёшь, пока не останавливаешься.'")

def quote2(request):
    return HttpResponse("Альберт Эйнштейн: 'Воображение важнее знания.'")

def quote3(request):
    return HttpResponse("Оскар Уайльд: 'Мы все рождаемся глупыми, но некоторые из нас решают остаться ими.'")