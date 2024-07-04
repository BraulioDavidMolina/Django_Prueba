from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import Archivos
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('matricula','carrera','turno')
        else:
            return('created','updated')
# ,'matricula','carrera','turno'

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    #list_filter = ('carrera','turno')

class AdministrarComentarioContacto(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensaje', 'created')
    search_fields = ('id', 'comentario')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    #list_filter = ('carrera','turno')
    
admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentario, AdministrarComentarios)
admin.site.register(ComentarioContacto, AdministrarComentarioContacto)
admin.site.register(Archivos)


