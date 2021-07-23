from django.forms import fields, forms, models
from django.contrib.auth.forms import UserCreationForm

from .models import *
class createuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']
