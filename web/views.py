from django.shortcuts import render
from web.models import Galery,Promos,Somos
from app.forms import CitasForm
# Create your views here.
def dashboard(request):
    galeria = Galery.objects.filter(activa=True)
    promos = Promos.objects.filter(activa=True)
    somos = Somos.objects.filter(activa=True).last()
    if request.method == "POST":
        form = CitasForm(request.POST)
        if form.is_valid():
            form.save()
    form = CitasForm()
    context ={
        "galeria":galeria,
        "promos":promos,
        "somos":somos,
        "form":form
    }
    return render(request, 'dashboard.html',context)