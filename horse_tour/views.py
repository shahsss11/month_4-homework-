from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def update_booking_view(request,id):
    booking_id = get_object_or_404(models.Booking, id=id)
    if request.method == 'POST':
        form = forms.BookingForm(request.POST, instance=booking_id)
        if form.is_valid():
            form.save()
            return redirect('/booking_list/')
    else:
        form = forms.BookingForm(instance=booking_id)
    return render(request, 'bookings/update_booking.html', {
        "form": form,
        'booking_id': booking_id,
    })

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
    return render(request, 'bookings/create_booking.html', {'form': form})

def booking_list_view(request):
    if request.method == "GET":
        booking = models.Booking.objects.all().order_by('-id')
    return render(request, 'bookings/booking_list.html', {'booking': booking})
    