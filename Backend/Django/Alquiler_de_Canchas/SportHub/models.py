from django.db import models

# Create your models here.
class Usuario(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Persona(models.Model):
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    NomYApell=models.CharField(max_length=30)
    Domicilio=models.CharField(max_length=30)
    DNI=models.IntegerField()
    Telefono=models.IntegerField()
    Fecha_Nac=models.DateField()   

class Productos(models.Model):
    Nombre_Producto=models.CharField(max_length=45)
    Descripcion=models.CharField(max_length=45)
    Stock=models.IntegerField()
    Precio=models.IntegerField()

class Cancha(models.Model):
    Suelo=models.CharField(max_length=45)  
    Cantidad=models.IntegerField()
    Descripcion=models.CharField(max_length=45)

class Torneo(models.Model):
    Nombre=models.CharField(max_length=45)
    Cant_participante=models.IntegerField()
    Descripcion=models.CharField(max_length=45)


# Claves foraneas de Usuario
class Niveles(models.Model):
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    Nivel_Tenis=models.CharField(max_length=10)
    Desafio=models.BooleanField()

# Claves foraneas de Productos
class Ventas(models.Model):
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    Productos=models.ForeignKey(Productos,on_delete=models.CASCADE)
    Cantidad=models.IntegerField()

class Facturas(models.Model):
    Ventas=models.ForeignKey(Ventas,on_delete=models.CASCADE)
    Codigo_Factura=models.IntegerField()

# Claves foraneas de Canchas, Torneo y Usuario:
class Inscripciones(models.Model):
    Torneo=models.ForeignKey(Torneo,on_delete=models.CASCADE)
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Canchas_Torneo(models.Model):
    Torneo=models.ForeignKey(Torneo,on_delete=models.CASCADE)
    Canchas=models.ForeignKey(Cancha,on_delete=models.CASCADE)

class Reservacion_Cancha(models.Model):
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    Cancha=models.ForeignKey(Cancha,on_delete=models.CASCADE)
    Horarios=models.DateField()   





