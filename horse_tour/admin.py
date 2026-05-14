from django.contrib import admin
from . import models

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    exclude = ('views',)