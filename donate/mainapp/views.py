from django import forms
from django.db import models
from django.http.request import validate_host
from django.shortcuts import render

import razorpay

# Key Id
# rzp_test_EIvzOOX7HqdWKM
# Key Secret
# A9PliJdX5Wb1SSPFejhTrDRv

PUBLIC_KEY = "rzp_test_EIvzOOX7HqdWKM"
SECRET_KEY = "A9PliJdX5Wb1SSPFejhTrDRv"

from. forms import DonationForm
from . import models
def index(request):
    donations = models.donation.objects.filter(paid=True)

    payment = None
    form = DonationForm()
    if request.method == "POST":
        form = DonationForm(data= request.POST)
        if form.is_valid():
            name = request.user
            about = form.cleaned_data.get('about')
            amount = form.cleaned_data.get('amount')*100

            client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))
            payment = client.order.create({
                'amount':amount, 
                'currency':'INR',
                'payment_capture':'1'
                })
            donation = models.donation(name = name, about=about, amount=amount, payment_id = payment['id']) 
            donation.save()
    return render(request, 'mainapp/index.html', {'form':form, 'payment':payment, 'donations':donations})


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST

        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val 
                break

        user = models.donation.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        
    return render(request, 'mainapp/success.html', {})
