from django import template
register = template.Library()

from app.models import FichaPaciente,IngresoEgresoFicha

@register.simple_tag
def getAbonos(id):
    tmp = FichaPaciente.objects.get(pk=id)
    ingresos = IngresoEgresoFicha.objects.filter(ficha=tmp)
    total = 0.0
    for item in ingresos:
        total = total + item.abono
    return "$"+str(total)