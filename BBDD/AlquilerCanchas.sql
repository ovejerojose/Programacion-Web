CREATE DATABASE AlquilerCanchas;

use AlquilerCanchas;

CREATE TABLE Usuario (
idCliente INT AUTO_INCREMENT,
NombreApellido VARCHAR(45) NOT NULL,
DNI INT,
Fecha_Nacimiento VARCHAR(30),
Domicilio VARCHAR(45),
email VARCHAR(80),
nivel_de_Tenis VARCHAR(4),
Telefono INT,
constraint pk_cliente primary key (idCliente)
);

CREATE TABLE Canchas_de_Tenis (
idCanchas_de_Tenis INT,
Tipo_de_Suelo VARCHAR(45),
Cantidad INT,
Descripcion VARCHAR(45),
constraint pk_Cancha primary key (idCanchas_de_Tenis)
);

CREATE TABLE Torneo (
idTorneo INT AUTO_INCREMENT,
Nombre VARCHAR(45),
Cant_participantes INT,
Descripcion VARCHAR(45),
constraint pk_Torneo primary key (idTorneo)
);

CREATE TABLE Productos (
idProductos INT NOT NULL,
Nombre_Producto VARCHAR(45),
Descripcion VARCHAR(45),
Cantidad INT,
Precio INT,
constraint pk_Producto primary key (idProductos)
); 

CREATE TABLE Reservacion_Cancha (
id_Horario DATE,
id_Cliente INT,
id_Cancha INT,
constraint fk_Clicli foreign key (id_Cliente) references Usuario(idCliente),
constraint fk_Cancan foreign key (id_Cancha) references Canchas_de_Tenis(idCanchas_de_Tenis)
);

CREATE TABLE Cancha_Torneo (
id_Torneo INT,
id_Cancha INT,
constraint fk_Cancan2 foreign key (id_Canchas) references Canchas_de_Tenis(idCanchas_de_Tenis),
constraint fk_Tortor foreign key (id_Torneo) references Torneo(idTorneo)
);

CREATE TABLE Inscripciones (
id_Cliente int,
id_Torneo int,
constraint fk_Clicli2 foreign key (id_Cliente) references Usuario(idCliente),
constraint fk_Tortor foreign key (id_Torneo) references Torneo(idTorneo)
);

CREATE TABLE Ventas (
idVentas INT,
id_cliente INT,
id_producto INT,
constraint pk_venta primary key (idVentas),
constraint fk_Clicli3 foreign key (id_cliente) references Usuario(idCliente),
constraint fk_Propro foreign key (id-producto) references Productos(idProductos)
);

CREATE TABLE Facturas (
id_Factura INT,
Id_Venta INT,
Codigo_Factura INT,
constraint pk_factura primary key (id_Factura),
constraint fk_venven foreign key (Id_Venta) references Ventas(idVentas)
);
 