from django.urls import path
from . import views


urlpatterns = [
    path('booking_list/', views.booking_list_view, name='bk_list'),
    path('booking_list/<int:id>/delete/', views.delete_booking_view, name='del_booking'),
    path('booking_list/<int:id>/update/', views.update_booking_view, name='edit_booking'),
    path('create_booking/', views.create_booking_view, name='crt_booking'),
    path('booking_list/<int:id>/', views.booking_detail_view, name='booking_detail')
]