from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404


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

