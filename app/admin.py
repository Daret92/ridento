from django.contrib import admin
from app.models import IngresoEgresoFicha,FichaPaciente,Paciente,Tratamientos
# Register your models here.
admin.site.register(Tratamientos)
admin.site.register(Paciente)
admin.site.register(FichaPaciente)
admin.site.register(IngresoEgresoFicha)
