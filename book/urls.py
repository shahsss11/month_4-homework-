from django.urls import path
from . import views


urlpatterns = [
    path('quote1/', views.quote1),
    path('quote2/', views.quote2),
    path('quote3/', views.quote3),
    path('', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),

]