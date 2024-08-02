from django.urls import path
from . import views
from trabajos import views as trabajosView
from experiencia import views as experienciasView
from educacion import views as educationView
from habilidades import views as skillsView

urlpatterns = [
    path('', views.inicio, name='home'),
    path('home/', views.about, name='paginaNosotros'),
    path('educacion/', educationView.education, name='paginaEducation'),
    path('experiencia/', experienciasView.experiencias, name='experiencia'),
    path('skills/', skillsView.skills, name='paginaSkills'),  # Correcto
    path('contacto/', views.contact, name='paginaContacto'),
    path('Proyectos/', trabajosView.proyecto, name='Proyectos'),
]

