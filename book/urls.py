from django.urls import path
from . import views


urlpatterns = [
    path('quote1/', views.quote1),
    path('quote2/', views.quote2),
    path('quote3/', views.quote3),
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]