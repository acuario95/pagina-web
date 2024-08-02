from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')



def experiencias(request):    
    return render(request, 'experiencia.html')

def skills(request):
    return render(request,'skills.html')

def contact(request):
    return render(request,'contact.html')


