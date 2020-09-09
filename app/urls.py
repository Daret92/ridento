
from django.urls import path

from app import views
urlpatterns = [
    path('index', views.index),
    path('logout', views.logout),
    path('indexT', views.indexTratamiento),
    path('indexP', views.indexProcedimiento),
    path('galeria', views.Galeria),
    path('promos', views.Promo),
    path('somos', views.SomosM),
    path('agenda', views.Agendados),
    path('historia', views.Historia),
    path('new_historial', views.NewHistoria),
    path('new_historial/<int:id>', views.NewHistoria),
    path('fichas_index', views.Fichas),
    path('new_ficha', views.NewFicha),
    path('getPaciente', views.getPaciente),
    path('seguimiento/<int:id>/<int:paciente>', views.Seguimiento),
    path('ieIndex', views.ieIndex),
    path('ieReporte', views.ieReporte),
]
    