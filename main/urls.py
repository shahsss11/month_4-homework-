from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('tour/', include('horse_tour.urls')),
]
