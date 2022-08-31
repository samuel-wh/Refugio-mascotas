from django import forms

# Importamos el modelo Mascota
from models import Mascota

# Clase del formulario mascota
class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        # Lista de los campos que utilizaremos del modelo
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'foto',
        ]

        # Etiquetas de los campos que se pintaran en el formularios
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
            'foto': 'Foto',
        }

        # Se pintan en forma de etiquetas html
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-info'}),
            'sexo': forms.TextInput(attrs={'class':'form-control border-info'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control border-info'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control border-info'}),
            'persona': forms.Select(attrs={'class':'form-control border-info'}),
            'vacuna': forms.CheckboxSelectMultiple(attrs={'class':'form-check-input border-info'}),
            
        }
