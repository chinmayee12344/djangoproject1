from django.forms import ModelForm

from .models import Order

from django import forms
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        