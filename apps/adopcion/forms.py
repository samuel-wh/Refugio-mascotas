

from django import forms

# Importamos el modelo Mascota
from models import Persona, Solicitud

# Clase del formulario mascota
class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        # Lista de los campos que utilizaremos del modelo
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]

        # Etiquetas de los campos que se pintaran en el formularios
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }

        # Se pintan en forma de etiquetas html
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-info'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control border-info'}),
            'edad': forms.TextInput(attrs={'class':'form-control border-info'}),
            'telefono': forms.TextInput(attrs={'class':'form-control border-info'}),
            'email': forms.TextInput(attrs={'class':'form-control border-info'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control border-info'}),
        }

# Clase del formulario solicitud
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]

        labels = {
            'numero_mascotas': 'Numero de mascota',
            'razones': 'Razones para adoptar',
        }
        widgets = {
            'numero_mascotas': forms.TextInput(attrs={'class':'form-control border-info'}),
            'razones': forms.Textarea(attrs={'class':'form-control border-info'}),
        }

    
