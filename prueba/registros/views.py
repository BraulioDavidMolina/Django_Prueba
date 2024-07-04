from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivo
from django.contrib import messages


# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos':alumnos})

#__    
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios':comentarios})
    form = ComentarioContactoForm()


def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentarios.html", {'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})



def editarComentarioContacto(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, "registros/editarComentario.html", {'comentario':comentario})


def guardarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)   
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/comentarios.html", {'comentarios': comentarios})
    return render(request, "registros/editarComentarios.html", {'comentario': comentario})


def contacto(request):
    return render(request, "registros/contacto.html")


def comentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'comentarios':comentarios})



def archivos(request):
    if request.method =='POST':
        form = FormArchivo(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion = descripcion, archivo=archivo)
            insert.save()
            return render(request, 'registros/archivos.html')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo': Archivos})








#Probando consultas ___________________________________________________________________________
def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

#__contains busquedas que contengan esa palabras
def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

#In verifica un intervalo de valores
def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

#__range Busqueda por rango de fechas
def consultar6(request):
    fechaInicio = datetime.date(2024, 7, 1)
    fechaFin = datetime.date(2024, 7, 3)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render(request,"registros/cosultas.html", {'alumnos':alumnos})

