
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import CreateRateCard, CreateCourier, CreateDestination
from . import views

urlpatterns = [   
    path('rate-card/add/', CreateRateCard.as_view(), name='create-rate-card'),
    path('courier/add/', CreateCourier.as_view(), name='create-courier'),
    path('destination/add/',
         CreateDestination.as_view(), name='create-destination'),
    path('min-kg-for-courier/',
         views.min_kg_for_courier_ajax, name='min-kg-for-courier'),  # AJax
]
