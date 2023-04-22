CREATE DATABASE AlquilerCanchas;

use AlquilerCanchas;

CREATE TABLE Cliente
(
Id_Cliente int auto_increment,
NombreApellido varchar(60) not null,
Email varchar(255) not null,
Telefono bigint(10),
Nivel_Tenis varchar(4),
Desafio varchar(4),
constraint pk_cliente primary key (Id_Cliente)
);

CREATE TABLE Profesores
(
Id_Profesores int auto_increment,
NombreApellido varchar(60) not null,
Email varchar(255) not null,
Telefono bigint(10),
Cliente_Id_Cliente int,
constraint pk_Profes primary key (Id_Profesores),
constraint fk_IdCli foreign key (Cliente_Id_Cliente) references Cliente(Id_Cliente)
);

CREATE TABLE Canchas
(
Id_Canchas int,
Horario datetime,
Estado varchar(4),
constraint pk_Cancha primary key (Id_Canchas)
);

CREATE TABLE Torneos
(
Id_Torneo int auto_increment,
Nombre varchar(45),
Categoria varchar(4),
constraint pk_Torneo primary key (Id_Torneo)
);

CREATE TABLE Cliente_Cancha
(
Cliente_Id_Cliente int,
Canchas_Id_Canchas int,
constraint fk_Clicli foreign key (Cliente_Id_Cliente) references Cliente(Id_Cliente),
constraint fk_Cancan foreign key (Canchas_Id_Canchas) references Canchas(Id_Canchas)
);

CREATE TABLE Profesores_Cancha
(
Profesores_Id_Profesores int,
Canchas_Id_Canchas int,
constraint fk_Propro foreign key (Profesores_Id_Profesores) references Profesores(Id_Profesores),
constraint fk_Cancan2 foreign key (Canchas_Id_Canchas) references Canchas(Id_Canchas),
);

CREATE TABLE Cancha_Torneo
(
Canchas_Id_Canchas int,
Torneo_Id_Torneo int,
constraint fk_Cancan3 foreign key (Canchas_Id_Canchas) references Canchas(Id_Canchas),
constraint fk_Tortor foreign key (Torneo_Id_Torneo) references Torneo(Id_Torneo),
);

CREATE TABLE Cliente_Torneo
(
Cliente_Id_Cliente int,
Torneo_Id_Torneo int,
constraint fk_Clicli2 foreign key (Cliente_Id_Cliente) references Cliente(Id_Cliente),
constraint fk_Tortor foreign key (Torneo_Id_Torneo) references Torneo(Id_Torneo)
);
 