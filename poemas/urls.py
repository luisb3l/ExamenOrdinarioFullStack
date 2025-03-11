from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_poemas, name='lista_poemas'),
]