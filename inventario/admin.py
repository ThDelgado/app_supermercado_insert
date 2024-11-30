from django.contrib import admin
from .models import Producto, Fabrica

		# Register your models here.

@admin.register(Fabrica)
class FabricaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','pais']
    search_fields = ['nombre' ] #filtro 
    ordering = ['nombre']



@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'f_vencimiento','fabrica']
    search_fields = ['nombre' ] #filtro 
    ordering = ['nombre']
