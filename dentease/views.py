from django.shortcuts import render,redirect
from .forms import ContactForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import User
from .forms import dentistForm
# Create your views here.

def dentistProfile(request):
    return render(request,"dentistProfile.html")

def dentistLanding(request):
    if request.user.is_authenticated:
        if request.user.is_startup:
            return HttpResponseRedirect(reverse('dentistProfile',kwargs={'pk': request.user.id}))
        else:
            template = "dentistLanding.html"
            return render(request,template)
    else:
        template = "dentistLanding.html"
        return render(request,template)



def dentistLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
    return render(request, "Dentist_Landing.html")
        # else:
        #     return render(request, "dentistLanding.html",{'error':'Invalid login details entered.'})

    # else:
    #     return redirect('dentistProfile') 

def dentistRegister(request):
     if request.method == 'POST':
        form = dentistForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dentistProfile')
     else:
        form = dentistForm()
     return render(request, "Dentist_registeration.html",{'forms': form})


def home(request):
    return render(request,"home.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'forms': form})   

   