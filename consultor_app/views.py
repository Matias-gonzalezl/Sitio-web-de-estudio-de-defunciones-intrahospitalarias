from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Estudio, Paciente, Region, Hospital



@login_required
def login (request) : # *** DEFINE VISTA DE NOMBRE home ****
    return (render (request, 'registration/login.html'))  # *** RETORNA  EL CONTENIDO DEL ARCHIVO HTML  index,html   ***

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def datos(request):
    reg = Region.objects.all()
    hosp = Hospital.objects.all()
    pac = Paciente.objects.all()
    context = {
        'pac': pac,
        'reg': reg,
        'hosp': hosp
    }
    print(type(pac))
    print(type(pac[0]))
    print('Fecha_def:', pac[0].fecha_def)

    print(type(Region.objects.values()))

    return render(request, 'datos.html', context)

@login_required
def get_regiones(request):
    regiones = list(Region.objects.values())

    if (len(regiones)):
        dicc = {
            'data': regiones
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def get_hospitales(request, id_region):
    hospitales = list(Hospital.objects.filter(id_region = id_region).values())

    if (len(hospitales)):
        dicc = {
            'data': hospitales
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def get_hospitales_v2(request):
    hospitales = list(Hospital.objects.values())

    if (len(hospitales)):
        dicc = {
            'data': hospitales
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def get_pacientes_reg(request, id_region):
    if (id_region == 0):
        pac = list(Paciente.objects.values())
    else:
        pac = list(Paciente.objects.filter(id_region = id_region).values())

    if (len(pac)):
        dicc = {
            'data': pac
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def get_pacientes_hosp(request, id_hosp):
    if (id_hosp == 0):
        pac = list(Paciente.objects.values())    
    else:
        pac = list(Paciente.objects.filter(id_hospital = id_hosp).values())

    if (len(pac)):
        dicc = {
            'data': pac
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def get_pacientes(request):
    pac = list(Paciente.objects.values())

    if (len(pac)):
        dicc = {
            'data': pac
        }
    else:
        dicc = {
            'data': 'No data.'
        }

    return JsonResponse(dicc)

@login_required
def estudio(request):

    if request.method == "POST":
        titulo = request.POST['titulo_estudio']
        cuerpo = request.POST['cuerpo_estudio']
        conclusion = request.POST['conclusion_estudio']

        estudio = Estudio.objects.create(
            titulo = titulo,
            cuerpo = cuerpo,
            conclusion = conclusion
        )

        estudio.save()

    return render(request, 'estudio.html')

@login_required
def recomendacion(request):
    
    region = Region.objects.all()
    hosp = Hospital.objects.all()
    context = {
        'regiones': region,
        'hospitales': hosp
    }

    return render(request, 'recomendacion.html', context)



