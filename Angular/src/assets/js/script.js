function mensajeRegistroExitoso(){
     
    var NombreDelGuapeton = document.getElementById("nombre_cliente").value;
    alert("Registro Exitosito v5, bievenido " + NombreDelGuapeton);
    document.getElementById("nombre_cliente").value = "";
    document.getElementById("domicilio").value = "";
    document.getElementById("fecha_de_nacimiento").value = "";
    document.getElementById("email_cliente").value = "";
    document.getElementById("telefonocelular").value = "";
    document.getElementById("opcion").value = "hidden";
    document.getElementById("radio").value = "";
    }