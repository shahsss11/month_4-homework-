from django.contrib import admin
from .models import TourCompany, Person, Review, Service, Horse

admin.site.register(TourCompany)
admin.site.register(Person)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Horse)