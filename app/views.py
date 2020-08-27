from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from app.models import Tratamientos,Procedimiento,Citas,Paciente
from app.forms import TratamientosForm,ProcedimientoForm,GaleryForm,PromosForm,SomosForm,PacienteForm
from web.models import Galery,Promos,Somos
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            do_login(request, user)
    
    if request.user.is_authenticated:
        context = {'latest_question_list': "latest_question_list"}
        return render(request, 'index.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('index')

def indexTratamiento(request):
    if request.user.is_authenticated:
        form = TratamientosForm()
        ids = False
        if request.method == 'POST':
            if request.POST.get("id"):
                subs = Tratamientos.objects.get(pk=request.POST.get("id"))
                tmp = TratamientosForm(request.POST,instance=subs)
            else:
                tmp = TratamientosForm(request.POST)
            if tmp.is_valid():
                tmp.save()
            else:
                print(tmp.errors)
        
        if request.method == 'GET':
            if request.GET.get("edit"):
                tmp = Tratamientos.objects.get(pk=request.GET["id"])
                ids = tmp.id
                form = TratamientosForm(instance=tmp)
            if request.GET.get("delete"):
                Tratamientos.objects.get(pk=request.GET["id"]).delete()
        

        tratamientos = Tratamientos.objects.all()
        
        context={
            "tratamientos":tratamientos,
            "form": form,
            "id":ids
        }
        return render(request,'indexT.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def indexProcedimiento(request):
    if request.user.is_authenticated:
        form = ProcedimientoForm()
        ids = False
        if request.method == 'POST':
            if request.POST.get("id"):
                subs = Procedimiento.objects.get(pk=request.POST.get("id"))
                tmp = ProcedimientoForm(request.POST,instance=subs)
            else:
                tmp = ProcedimientoForm(request.POST)
            if tmp.is_valid():
                tmp.save()
            else:
                print(tmp.errors)
        
        if request.method == 'GET':
            if request.GET.get("edit"):
                tmp = Procedimiento.objects.get(pk=request.GET["id"])
                ids = tmp.id
                form = ProcedimientoForm(instance=tmp)
            if request.GET.get("delete"):
                Procedimiento.objects.get(pk=request.GET["id"]).delete()
        

        procedimiento = Procedimiento.objects.all()
        
        context={
            "tratamientos":procedimiento,
            "form": form,
            "id":ids
        }
        return render(request,'indexP.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def Galeria(request):
    if request.user.is_authenticated:
        form =GaleryForm()
        ids = False
        if request.method == 'POST':
            if request.POST.get("id"):
                subs = Galery.objects.get(pk=request.POST.get("id"))
                tmp = GaleryForm(request.POST,request.FILES,instance=subs)
                print(tmp)
            else:
                tmp = GaleryForm(request.POST,request.FILES)

            if tmp.is_valid():
                tmp.save()
            else:
                print(tmp.errors)

        if request.method == 'GET':
            if request.GET.get("edit"):
                tmp = Galery.objects.get(pk=request.GET["id"])
                ids = tmp.id
                form = GaleryForm(instance=tmp)
            if request.GET.get("delete"):
                Galery.objects.get(pk=request.GET["id"]).delete()


        galeria = Galery.objects.all()

        context={
            "galeria":galeria,
            "form":form,
            "id":ids
        }
        return render(request,'galeria.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def Promo(request):
    if request.user.is_authenticated:
        form =PromosForm()
        ids = False
        if request.method == 'POST':
            if request.POST.get("id"):
                subs = Promos.objects.get(pk=request.POST.get("id"))
                tmp = PromosForm(request.POST,request.FILES,instance=subs)
            else:
                tmp = PromosForm(request.POST,request.FILES)

            if tmp.is_valid():
                tmp.save()
            else:
                print(tmp.errors)

        if request.method == 'GET':
            if request.GET.get("edit"):
                tmp = Promos.objects.get(pk=request.GET["id"])
                ids = tmp.id
                form = PromosForm(instance=tmp)
            if request.GET.get("delete"):
                Promos.objects.get(pk=request.GET["id"]).delete()
        
        promos = Promos.objects.all()
        
        context={
            "promos":promos,
            "form":form,
            "id":ids
        }
        return render(request,'promociones.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def SomosM(request):
    if request.user.is_authenticated:
        form =SomosForm()
        ids = False
        if request.method == 'POST':
            if request.POST.get("id"):
                subs = Somos.objects.get(pk=request.POST.get("id"))
                tmp = SomosForm(request.POST,instance=subs)
            else:
                tmp = SomosForm(request.POST)

            if tmp.is_valid():
                tmp.save()
            else:
                print(tmp.errors)

        if request.method == 'GET':
            if request.GET.get("edit"):
                tmp = Somos.objects.get(pk=request.GET["id"])
                ids = tmp.id
                form = SomosForm(instance=tmp)
            if request.GET.get("delete"):
                Somos.objects.get(pk=request.GET["id"]).delete()
        
        somos = Somos.objects.all()
        
        context={
            "somos":somos,
            "form":form,
            "id":ids
        }
        return render(request,'somos.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def Agendados(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            if request.GET.get("agendado"):
                tmp = Citas.objects.get(pk=request.GET.get("id"))
                tmp.agendado = True
                tmp.save()
            if request.GET.get("delete"):
                Citas.objects.get(pk=request.GET["id"]).delete()

        agenda = Citas.objects.all()
        context ={
            "agendado": agenda
        }
        return render(request,'agendados.html',context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def Historia(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.all()
        if request.method == "GET":
            if request.GET.get("edit"):
                return redirect(NewHistoria,id=request.GET.get("id"))
            if request.GET.get("delete"):
                Paciente.objects.get(pk=request.GET.get("id")).delete()
                return redirect(Historia)
        context={
            "pacientes":pacientes
        }
        return render(request,"historia/index.html",context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def NewHistoria(request,id = None):
    if request.user.is_authenticated:
        ids = id
        form = PacienteForm()
        
        if id != None:
            historial = Paciente.objects.get(pk=id)
            form = PacienteForm(instance=historial)
        
        if request.method=="POST":
            if request.POST.get("id"):
                historial = Paciente.objects.get(pk=request.POST.get("id"))
            else:
                historial = None
            form = PacienteForm(request.POST,request.FILES,instance=historial)
            
            if form.is_valid():
                obj = form.save(commit=False)
                if historial == None:
                    obj.token = get_random_string(length=6)
                else:
                    print(historial.token)
                    obj.token = historial.token
                obj.save()
                return redirect(Historia)
            else:
                print(form.errors)
                form = PacienteForm(request.POST)

        
        context={
            "form":form,
            "id":ids
        }
        return render(request,"historia/new.html",context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})