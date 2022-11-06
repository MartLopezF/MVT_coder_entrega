from django.shortcuts import render
from .models import Familiares

# Create your views here.

def home(request):
    familia = Familiares.objects.all()
    datos = {
        'familiares': familia

    }
    
    return render(request, 'app/home.html', datos)


