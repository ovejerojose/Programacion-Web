

class Producto:
    
    def __init__(self, idProducto, nombre, descripcion, cantidad, precio) :
        self._idProducto = idProducto
        self._nombre = nombre
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._precio = precio
    
    def mostrar_producto(self):
        print(f' Producto: {self._idProducto} {self._nombre} {self._descripcion} {self._cantidad} {self._precio}')
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @descripcion.setter
    def descripcon(self, descripcion):
        self._descripcion = descripcion
        
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
        
    @precio.setter
    def precio(self, precio):
        self._precio = precio


class Usuario:
    def __init__(self, idCliente, nombre, dni, domicilio, email, nivelTenis, telefono) :
        self._idCliente = idCliente
        self._nombre = nombre
        self._dni = dni
        self._domicilio = domicilio
        self._email = email
        self._nivelTenis = nivelTenis
        self._telefono = telefono
        
    def mostrar_usuario(self):
        print(f' Usuario: {self._idCliente} {self._nombre} {self._email} {self._nivelTenis} {self._telefono}')
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @email.setter
    def email(self, email):
        self._email = email
    
    @nivelTenis.setter
    def nivelTenis(self, nivelTenis):
        self._nivelTenis = nivelTenis
    
    @domicilio.setter
    def domicilio(self, domicilio):
        self._domicilio = domicilio
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono
        

class Torneo:
    
    def __init__ (self, idTorneo, nombre, cantidad, descripcion):
        self._idTorneo = idTorneo
        self._nombre = nombre
        self._cantidad = cantidad
        self._descripcion = descripcion
    
    

class CanchaTenis:
    def __init__(self, idCancha, tipo, cantidad, descripcion):
        self._idCancha = idCancha
        self._tipo = tipo
        self._cantidad = cantidad
        self._descripcion = descripcion
    
    