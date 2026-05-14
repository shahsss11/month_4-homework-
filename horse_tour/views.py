from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import F
from . import models, forms


def update_booking_view(request, id):
    booking_id = get_object_or_404(models.Booking, id=id)
    if request.method == 'POST':
        form = forms.BookingForm(request.POST, instance=booking_id)
        if form.is_valid():
            form.save()
            return redirect('/booking_list/')
    else:
        form = forms.BookingForm(instance=booking_id)

    return render(request, 'bookings/update_booking.html', {"form": form,'booking_id': booking_id,})


def delete_booking_view(request, id):
    booking_id = get_object_or_404(models.Booking, id=id)
    booking_id.delete()
    return redirect('/booking_list/')


def create_booking_view(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/booking_list/')
    else:
        form = forms.BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form,})


def booking_list_view(request):
    search = request.GET.get('search', '')
    bookings = models.Booking.objects.all().order_by('-id')
    if search:
        bookings = bookings.filter(company__name__icontains=search)
    paginator = Paginator(bookings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookings/booking_list.html', {'page_obj': page_obj,'search': search})

def booking_detail_view(request, id):
    booking = get_object_or_404(models.Booking, id=id)

    booking.views += 1
    booking.save()

    return render(request, 'bookings/booking_detail.html', {'booking': booking})