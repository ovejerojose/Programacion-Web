from django.db import models

class CarritoCompras(models.Model):
    producto_nombre=models.CharField(max_length=45)
    producto_precio=models.DecimalField(max_length=10,blank=False,decimal_places=2,max_digits=10)
    producto_cantidad=models.PositiveIntegerField()