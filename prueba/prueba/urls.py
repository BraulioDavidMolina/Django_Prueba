"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('contacto/',views_registros.contacto, name="Contacto"),
    path('registro/',views.registro, name="Registro"),
    path('ejemplo/',views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('comentarios/', views_registros.comentarios, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('guardarComentario/<int:id>/', views_registros.guardarComentarioContacto, name='Guardar'),
    path('subir/', views_registros.archivos, name="Subir"),
    #Consultas
    path('consultas1/',views_registros.consultar1, name="Consultas"),
    path('consultas2/',views_registros.consultar2, name="Consultas2"),
    path('consultas3/',views_registros.consultar3, name="Consultas3"),
    path('consultas4/',views_registros.consultar4, name="Consultas4"),
    path('consultas5/',views_registros.consultar5, name="Consultas5"),
    path('consultas6/',views_registros.consultar6, name="Consultas6"),
    path('consultas7/',views_registros.consultar7, name="Consultas7"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)