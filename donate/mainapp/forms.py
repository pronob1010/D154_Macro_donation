
from django import forms
from . models import *

class DonationForm(forms.ModelForm):
    class Meta:
        model = donation
        fields = ['about','amount']
