from django.shortcuts import render

# Create your views here.
from. forms import DonationForm
def index(request):
    form = DonationForm()
    if request.method == "POST":
        form = DonationForm(data= request.POST)
        if form.is_valid():
            print(form)
    return render(request, 'mainapp/index.html', {'form':form})



def success(request):
    return render(request, 'mainapp/success.html', {})
