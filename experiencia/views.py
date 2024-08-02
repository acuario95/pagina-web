
from django.shortcuts import render
from .models import Experiencia

def experiencias(request):
    listarexperiencias = Experiencia.objects.all()
    print(listarexperiencias) 
    return render(request, 'experiencia.html', {'experiencias':listarexperiencias})