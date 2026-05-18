from django.shortcuts import redirect
from django.views import generic
from . import models, forms


class UpdateBookingView(generic.UpdateView):
    template_name = 'bookings/update_booking.html'
    form_class = forms.BookingForm
    model = models.Booking
    success_url = '/booking_list/'
    context_object_name = 'booking_id'


class DeleteBookingView(generic.DeleteView):
    model = models.Booking
    success_url = '/booking_list/'


class CreateBookingView(generic.CreateView):
    template_name = 'bookings/create_booking.html'
    form_class = forms.BookingForm
    success_url = '/booking_list/'


class BookingListView(generic.ListView):
    template_name = 'bookings/booking_list.html'
    context_object_name = 'page_obj'
    model = models.Booking
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        bookings = self.model.objects.all().order_by('-id')

        if search:
            bookings = bookings.filter(company__name__icontains=search)

        return bookings
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class BookingDetailView(generic.DetailView):
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'
    model = models.Booking

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj