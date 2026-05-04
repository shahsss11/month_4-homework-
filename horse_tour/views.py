from django.shortcuts import render
from .models import TourCompany, Review


def horse_tour(request):
    tours = TourCompany.objects.all()
    reviews = Review.objects.all()

    return render(request, 'horse_tour/horse_tour.html', {
        'companies': tours,
        'reviews': reviews
    })