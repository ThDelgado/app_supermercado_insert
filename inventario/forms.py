from django.forms import ModelForm    
from django import forms     
 
from .models import Producto

class ProductoFormAdd(ModelForm):    # cLASES EN UPPERCAMELCASE
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'descripcion', 
            'precio', 
            'fabrica',
            'f_vencimiento',
            ]

    
        labels = {
            "descripcion": ("Descripción"),
            "fabrica": ("Fabrica"),
        }
        
        help_texts = {
            "nombre": ("* El nombre debe contener sólo letras, espacio, -"),
            "precio": ("* El precio debe ser mayor a 0"),
        }
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "descripcion": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": 'form-control', 'min': 1}),
            "fabrica": forms.Select(attrs={"class": 'form-control'}),
            "f_vencimiento": forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
        }
    
