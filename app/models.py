from django.db import models

# Create your models here.
class Tratamientos(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)

class Procedimiento(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)

class Citas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10,unique=True)
    agendado = models.BooleanField(default=False)

    

SEXO = [
    ('H', 'Hombre'),
    ('M', 'Mujer'),
]

ESTADO = [
    ('S', 'Soltero'),
    ('C', 'Casado'),
    ('D', 'Divorciado'),
    ('V', 'Viudo'),
    ('U', 'Union Libre'),
]
COMIDA = [
    ('B','Buena'),
    ('R','Regular'),
    ('D','Deficiente'),
]
BAÑO = [
    ('1','1 a la Semana'),
    ('2','2 - 3 a la Semana '),
    ('3','Diario'),
]
class Paciente(models.Model):
    token = models.CharField(max_length=6,blank=True)
    alta = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXO, max_length=10)
    estado_civil = models.CharField(choices=ESTADO, max_length=20)
    edad = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    responsable = models.CharField(max_length=50)
    telefono_responsable = models.CharField(max_length=10)
    diabetes = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    cardiovascular = models.BooleanField(default=False)
    asma = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    reumatismos = models.BooleanField(default=False)
    sida = models.BooleanField(default=False)
    epilepsia = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    hemofilia = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=500,blank=True)
    personal_epilepsia = models.BooleanField(default=False)
    personal_cardiopatias = models.BooleanField(default=False)
    personal_cardiopatia_cual = models.CharField(max_length=100,blank=True)
    personal_tosferina = models.BooleanField(default=False)
    personal_paludismo = models.BooleanField(default=False)
    personal_hepatitis = models.BooleanField(default=False)
    personal_hemorragias = models.BooleanField(default=False)
    personal_vih = models.BooleanField(default=False)
    persona_alergias = models.BooleanField(default=False)
    personal_alergias_cual = models.CharField(max_length=100,blank=True)
    personal_hipertencion = models.BooleanField(default=False)
    personal_amigdalitis = models.BooleanField(default=False)
    personal_hipotension = models.BooleanField(default=False)
    personal_parasitos = models.BooleanField(default=False)
    personal_ets = models.BooleanField(default=False)
    personal_diabetes = models.BooleanField(default=False)
    personal_sarampion = models.BooleanField(default=False)
    personal_padecio_infancia = models.CharField(max_length=500,blank=True)
    personal_sangre = models.BooleanField(default=False)
    personal_sangre_porque = models.CharField(max_length=100,blank=True)
    personal_fracturas = models.BooleanField(default=False)
    personal_fractura_donde = models.CharField(max_length=50,blank=True)
    personal_operacion = models.BooleanField(default=False)
    personal_operacion_de = models.CharField(max_length=100,blank=True)
    personal_operacion_evolucion = models.CharField(max_length=100,blank=True)
    personal_alergia_medicamento = models.BooleanField(default=False)
    personal_alergia_medicamento_cual = models.CharField(max_length=100,blank=True)
    personal_infeccion = models.BooleanField(default=False)
    personal_tratamiento_medico = models.BooleanField(default=False)
    personal_tratamiento_medico_cual = models.CharField(max_length=100,blank=True)
    personal_paciente_coopera = models.BooleanField(default=False)
    personal_orientado = models.BooleanField(default=False)
    personal_complexion = models.CharField(max_length=50,blank=True)
    personal_facies = models.CharField(max_length=50,blank=True)
    personal_comentarios = models.CharField(max_length=100,blank=True)
    casa_agua_potable = models.BooleanField(default=False)
    casa_luz = models.BooleanField(default=False)
    casa_drenaje = models.BooleanField(default=False)
    casa_habitacion_ventilacion = models.BooleanField(default=False)
    casa_habitacion_iluminada = models.BooleanField(default=False)
    casa_construccion = models.CharField(max_length=50,blank=True)
    casa_promiscuidad = models.CharField(max_length=50,blank=True)
    casa_hacinamiento = models.CharField(max_length=50,blank=True)
    alimentacion = models.CharField(choices=COMIDA, max_length=20,blank=True)
    frecuencia_baño = models.CharField(choices=BAÑO, max_length=20,blank=True)
    cambio_ropa = models.CharField(max_length=20,blank=True)
    cepillado_dental = models.CharField(max_length=20,blank=True)
    metodo_cepillado = models.CharField(max_length=20,blank=True)
    hilo_dental = models.CharField(max_length=20,blank=True)
    hilo_dental_frecuencia = models.CharField(max_length=20,blank=True)
    enjuages_bucales = models.BooleanField(default=False)
    enjuage_marca = models.CharField(max_length=20,blank=True)
    enjuage_frecuencia = models.CharField(max_length=20,blank=True)
    tabaquismo = models.BooleanField(default=False)
    toxicomania = models.BooleanField(default=False,blank=True)
    toxicomania_tipo = models.CharField(max_length=20,blank=True)
    alcohol = models.BooleanField(default=False)
    frecuencia_alchol = models.CharField(max_length=20,blank=True)
    tatuaje = models.BooleanField(default=False)
    vacunas = models.CharField(max_length=10,blank=True)
    deporte = models.CharField(max_length=20,blank=True)
    motivo_consulta = models.CharField(max_length=1000,blank=True)
    teraputica_rostro = models.CharField(max_length=100,blank=True)
    teraputica_encia = models.CharField(max_length=100,blank=True)
    teraputica_labios = models.CharField(max_length=100,blank=True)
    teraputica_paladar_carrillos= models.CharField(max_length=100,blank=True)
    lengua_macrodoncia = models.BooleanField(default=False)
    lengua_microdoncia = models.BooleanField(default=False)
    lengua_escrota = models.BooleanField(default=False)
    lengua_bifida = models.BooleanField(default=False)
    lengua_saburral = models.BooleanField(default=False)
    lengua_color = models.CharField(max_length=20,blank=True)
    lengua_musculos = models.CharField(max_length=20,blank=True)
    lengua_atm_izq = models.CharField(max_length=20,blank=True)
    lengua_atm_derecha = models.CharField(max_length=20,blank=True)
    lengua_observaciones = models.CharField(max_length=500,blank=True)
    odontograma = models.ImageField(upload_to="odontograma",blank=True)
    estudios_auxiliares = models.CharField(max_length=200,blank=True)
    diagnostico = models.CharField(max_length=1500,blank=True)
    pronostico = models.CharField(max_length=1500,blank=True)
    plan_tratamiento = models.CharField(max_length=1500,blank=True)
    paciente_suscribe = models.CharField(max_length=1500,blank=True)
    firma_paciente = models.ImageField(upload_to="paciente",blank=True)



