from django.shortcuts import render
from .models import Proyecto


# Create your views here.

def proyecto(request):
    listarProyectos = Proyecto.objects.all()
    return render(request,'Proyectos.html', {'proyectos': listarProyectos})