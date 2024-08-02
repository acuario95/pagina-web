from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige a una página de éxito o agradecimiento
    else:
        form = ContactoForm()
    return render(request, 'contact.html', {'form': form})
