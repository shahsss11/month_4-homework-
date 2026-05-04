from django.urls import path
from .views import horse_tour

urlpatterns = [
    path('', horse_tour, name='horse_tour'),
]