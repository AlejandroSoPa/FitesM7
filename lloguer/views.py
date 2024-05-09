from django.shortcuts import render
from .models import Automobil

# Create your views here.
def menu(request):
    automobils = Automobil.objects.all()
    return render(request, 'menu.html', {'automobils': automobils})