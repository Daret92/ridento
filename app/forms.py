from django import forms
from app.models import Tratamientos,Procedimiento,Citas,Paciente,FichaPaciente,IngresoEgresoFicha,GastosDiarios
from web.models import Galery,Promos,Somos
class TratamientosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TratamientosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Tratamientos
        fields = '__all__'
        widgets = {
               'descripcion': forms.Textarea(attrs={'cols': 25, 'rows': 10}),
           }

class ProcedimientoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcedimientoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Procedimiento
        fields = '__all__'
        widgets = {
               'descripcion': forms.Textarea(attrs={'cols': 25, 'rows': 10}),
           }

class GaleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GaleryForm, self).__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Galery
        fields = '__all__'
        widgets = {
               'texto': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
           }

class PromosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PromosForm, self).__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Promos
        fields = '__all__'
        widgets = {
               'texto': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
           }



class SomosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SomosForm, self).__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Somos
        fields = '__all__'
        widgets = {
               'texto': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
           }


class CitasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CitasForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Citas
        exclude =('agendado',)

class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for item in self.fields:
            if item != "firma_paciente" and item != "odontograma":
                self.fields[item].widget.attrs['class'] = 'form-control'
        self.fields["token"].widget.attrs['hidden'] = 'true'
        
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
                'observaciones': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
                'personal_padecio_infancia': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'personal_comentarios': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'motivo_consulta': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'lengua_musculos': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'lengua_atm_izq': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'lengua_atm_derecha': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'lengua_observaciones': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'estudios_auxiliares': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'diagnostico': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'pronostico': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
                'plan_tratamiento': forms.Textarea(attrs={'cols': 25, 'rows': 3}),
           }

class FichaPacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FichaPacienteForm, self).__init__(*args, **kwargs)
        for item in self.fields:
            self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = FichaPaciente
        fields = '__all__'
        widgets = { 
            'procedimiento': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
        }


class IngresoEgresoFichaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngresoEgresoFichaForm, self).__init__(*args, **kwargs)
        for item in self.fields:
            if item != "tarjeta" and item != "transferencia" and item != "efectivo":
                self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = IngresoEgresoFicha
        fields = '__all__'

class GastosDiariosForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GastosDiariosForm, self).__init__(*args, **kwargs)
        for item in self.fields:
            if item != "tarjeta" and item != "transferencia" and item != "efectivo":
                self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = GastosDiarios
        exclude = ('user',)

    