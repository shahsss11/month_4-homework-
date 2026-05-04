from django.urls import path
from . import views


urlpatterns = [
    path('quote1/', views.quote1),
    path('quote2/', views.quote2),
    path('quote3/', views.quote3),
]