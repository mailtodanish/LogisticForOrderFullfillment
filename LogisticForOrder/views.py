from django.shortcuts import render
from .form import RateCardCreateForm, CourierCreateForm, DestinationCreateForm
from .models import Rate, CourierAgency, Destination
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
        context['records'] = Rate.objects.all().order_by('courier', 'from_destination')
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


@csrf_exempt
def min_kg_for_courier_ajax(request):
    '''
    Returns Minimum KG for Courier
    '''
    if request.method == 'POST':
        pk = request.POST.get('pk')
        courier = CourierAgency.objects.get(pk=pk)
        data = {'min_kg': courier.min_kg}
        return JsonResponse(data)
    else:
        data = {'min_kg': ''}
        return JsonResponse(data)


@csrf_exempt
def calculateQuotationForCourier(request):
    if request.method == 'POST':
        from_destination = request.POST.get('from_destination')
        to_destination = request.POST.get('to_destination')
        weight = request.POST.get('weight')
        courier = CourierAgency.objects.all()
        From = Destination.objects.filter(name=from_destination)
        to = Destination.objects.filter(name=to_destination)
        rates = Rate.objects.filter(from_destination=From and to=to)
        if rates.exists():
        data = {'min_kg': courier.min_kg}
        return JsonResponse(data)
    else:
        data = {'min_kg': ''}
        return JsonResponse(data)
