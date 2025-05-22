from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioTienda, name='indexTienda'),
    path('nuevaTienda', views.nuevaTienda, name='nuevaTienda'),
    path('guardarTienda', views.guardarTienda, name='guardarTienda'),
    path('eliminarTienda/<id>', views.eliminarTienda, name='eliminarTienda'),
    path('editarTienda/<id>', views.editarTienda, name='editarTienda'),
    path('procesarEdicionTienda/<id>', views.procesarEdicionTienda, name='procesarEdicionTienda'),
]
