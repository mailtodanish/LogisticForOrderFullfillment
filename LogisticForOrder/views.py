from django.shortcuts import render
from .form import RateCardCreateForm, CourierCreateForm, DestinationCreateForm
from .models import Rate, CourierAgency, Destination
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class CreateRateCard(FormView):
    '''
    Create rate card of each courier
    '''
    form_class = RateCardCreateForm
    success_url = reverse_lazy('create-rate-card')
    template_name = 'LogisticForOrder/add_rate_card.html'
    model = Rate
    initial = {}

    def form_valid(self, form):
        notes = form.save(commit=False)
        notes.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = Rate.objects.all().order_by('courier')
        return context


class CreateCourier(FormView):
    '''
    add courier agencies
    '''
    form_class = CourierCreateForm
    success_url = reverse_lazy('create-courier')
    template_name = 'LogisticForOrder/add_courier.html'
    model = CourierAgency
    initial = {}

    def form_valid(self, form):
        notes = form.save(commit=False)
        notes.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = CourierAgency.objects.all().order_by('name')
        return context


class CreateDestination(FormView):
    '''
    add destination (To & From) agencies
    '''
    form_class = DestinationCreateForm
    success_url = reverse_lazy('create-destination')
    template_name = 'LogisticForOrder/add_destination.html'
    model = Destination
    initial = {}

    def form_valid(self, form):
        notes = form.save(commit=False)
        notes.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = Destination.objects.all().order_by('name')
        return context
