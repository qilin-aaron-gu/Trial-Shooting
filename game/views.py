from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView, ListView,DetailView,TemplateView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

# user signup
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('csg:home')
    else:
        form = UserSignUpForm()
    return render(request, 'registration.html', {'form': form})

class HowView(TemplateView):
    template_name = 'how.html'

def download(request):
    return render(request, 'download.html')

def zip_file_view_windows(request):
    response = HttpResponse(open('Main.zip', 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=Game_windows_version.zip'
    return response

def zip_file_view_mac(request):
    response = HttpResponse(open('Mainm.zip', 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=Game_mac_version.zip'
    return response

def support(request):
    return render(request, 'support.html')

def reflection(request):
    return render(request, 'reflection.html')