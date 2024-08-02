from django.urls import path
from django.views.generic import TemplateView
from .views import contacto_view

urlpatterns = [
     path('contacto/', contacto_view, name='paginaContacto'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),  # Página de éxito
]
