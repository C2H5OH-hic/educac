from django import forms
from .models import Experimento
from apps.horarios.models import Horario  # Importa el modelo Horario

class ExperimentoForm(forms.ModelForm):
    class Meta:
        model = Experimento
        fields = ['nombre', 'descripcion', 'materiales', 'procedimiento', 'fecha', 'contenido', 'asignado_a', 'horario']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'materiales': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'procedimiento': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'asignado_a': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),  # Selector para horarios
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra los horarios que no están asignados a ningún experimento
        self.fields['horario'].queryset = Horario.objects.filter(experimento=None)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
