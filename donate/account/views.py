from django.contrib.auth import authenticate, forms, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from . forms import createuser
def signup_user(request):
    form = createuser()
    if request.method == "POST":
        form = createuser(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    return render(request, 'account/signup.html', {'form':form})

from django.contrib.auth.forms import AuthenticationForm
def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'account/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
