
from django.urls import path
from . import views

urlpatterns = [
    path('experiencias/', views.experiencias, name='experiencias'),
]
