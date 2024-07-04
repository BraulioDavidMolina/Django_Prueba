from django import forms
from .models import ComentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']
        
#Funcion que permite que se limpie la base de datos al momento de hacer un cambio en el archibo
class CustomClearableFileInput(ClearableFileInput):
    templete_with_clear = '<br> <labelfor="%(clear_checkbox_id)s">%(clear_checkbox_label)s</labelfor=> %(clear)s'
    
    
class FormArchivo(ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo','descripcion', 'archivo')
        widgets = {
            'archivos': CustomClearableFileInput
            }