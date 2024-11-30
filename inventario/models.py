from django.db import models
from django.utils import timezone


class Fabrica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True,blank=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'fabricas'

    def __str__(self):   
	    return self.nombre




class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)  
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    precio = models.PositiveIntegerField(blank=False, null=False, default=999999)
    fabrica = models.ForeignKey(Fabrica, models.DO_NOTHING,blank=True, null=True)
    f_vencimiento = models.DateField(default=timezone.now,blank=False, null=False )
    
    
    class Meta:
        managed = True
        db_table = 'productos'
        
    def __str__(self):   
        return self.nombre