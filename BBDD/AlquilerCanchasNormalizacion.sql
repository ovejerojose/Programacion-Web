CREATE DATABASE AlquilerCanchas;

use AlquilerCanchas;

CREATE TABLE Usuario (
idCliente INT AUTO_INCREMENT,
ClavePrivada VARCHAR(45) NOT NULL,
IdPersona INT, 
email VARCHAR(80) NOT NULL,
ID_Nivel INT,
constraint pk_cliente primary key (idCliente),
constraint fk_PerPer foreign key (IdPersona) references Persona(idPersona),
constraint fk_NivNiv foreign key (ID_Nivel) references Niveles(idNivel)
);

CREATE TABLE Persona (
idPersona INT AUTO_INCREMENT,
Nombre VARCHAR(45),
Apellido VARCHAR(45),
DNI INT,
Fecha_Nac VARCHAR(45),
Telefono VARCHAR(45),
Domicilio VARCHAR(45),
constraint pk_Persona primary key (idPersona)
);

CREATE TABLE Niveles (
idNivel INT,
Nivel INT,
constraint pk_Nivel primary key (idNivel)
);

CREATE TABLE Canchas_de_Tenis (
idCanchas_de_Tenis INT NOT NULL,
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
Stock INT,
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
idVentas INT AUTO_INCREMENT,
id_cliente INT,
id_producto INT,
Cantidad INT,
constraint pk_venta primary key (idVentas),
constraint fk_Clicli3 foreign key (id_cliente) references Usuario(idCliente),
constraint fk_Propro foreign key (id_producto) references Productos(idProductos)
);

CREATE TABLE Facturas (
id_Factura INT AUTO_INCREMENT,
Id_Venta INT,
Codigo_Factura INT,
constraint pk_factura primary key (id_Factura),
constraint fk_venven foreign key (Id_Venta) references Ventas(idVentas)
);
 