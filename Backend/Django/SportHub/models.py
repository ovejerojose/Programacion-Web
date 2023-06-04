
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.
####Api Rest####
class CustomUser(AbstractUser):
    email=models.EmailField(max_length=150,unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','password']
    groups = models.ManyToManyField(Group, related_name='custom_users', related_query_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', related_query_name='custom_user')

class MyModel(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='mymodels')



class Personas(models.Model):
    Usuario=models.ForeignKey(CustomUser, on_delete=models.CASCADE)    
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
class Nivel(models.Model):
    Usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE)    
    Nivel_Tenis=models.CharField(max_length=10)
    Desafio=models.BooleanField()

# Claves foraneas de Productos
class Venta(models.Model):
    Usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Productos=models.ForeignKey(Productos,on_delete=models.CASCADE)
    Cantidad=models.IntegerField()

class Factura(models.Model):
    Ventas=models.ForeignKey(Venta,on_delete=models.CASCADE)
    Codigo_Factura=models.IntegerField()

# Claves foraneas de Canchas, Torneo y Usuario:
class Inscripcion(models.Model):
    Torneo=models.ForeignKey(Torneo,on_delete=models.CASCADE)
    Usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Canchas_Torneo(models.Model):
    Torneo=models.ForeignKey(Torneo,on_delete=models.CASCADE)
    Canchas=models.ForeignKey(Cancha,on_delete=models.CASCADE)

class Reservaciones_Cancha(models.Model):
    Usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE)    
    Cancha=models.ForeignKey(Cancha,on_delete=models.CASCADE)
    Horarios=models.DateField()   

