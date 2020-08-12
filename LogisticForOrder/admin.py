from django.contrib import admin
from .models import CourierAgency, Destination, Rate

admin.site.register(CourierAgency)
admin.site.register(Destination)
admin.site.register(Rate)
