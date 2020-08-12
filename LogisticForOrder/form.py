from django import forms
from .models import Rate, CourierAgency, Destination


class RateCardCreateForm(forms.ModelForm):
    '''
    Rate Card Create Form
    '''

    class Meta:
        model = Rate
        fields = '__all__'


class CourierCreateForm(forms.ModelForm):
    '''
    Courier Create Form
    '''

    class Meta:
        model = CourierAgency
        fields = ['name', ]


class DestinationCreateForm(forms.ModelForm):
    '''
    Courier Create Form
    '''

    class Meta:
        model = Destination
        fields = ['name', ]
