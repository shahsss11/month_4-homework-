from django.urls import path
from . import views


urlpatterns = [
    path('booking_list/', views.BookingListView.as_view(), name='bk_list'),
    path('booking_list/<int:pk>/delete/', views.DeleteBookingView.as_view(), name='del_booking'),
    path('booking_list/<int:pk>/update/', views.UpdateBookingView.as_view(), name='edit_booking'),
    path('create_booking/', views.CreateBookingView.as_view(), name='crt_booking'),
    path('booking_list/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail')
]