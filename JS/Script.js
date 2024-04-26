

function validar(){
    var correo = document.getElementById('correoUsuario').value
    var error=[];
    var confirmacion=0
    
    var nombre = document.getElementById('nombreUsuario').value
    
     
    
    if (nombre ==''){
        error.push('Nombre')
        confirmacion=1  
        

    }   
    

    var apellido = document.getElementById('apellidoPaterno').value
    if (apellido ==''){
        error.push('Apellido paterno')
        confirmacion=1
        
    }

    var apellidoM = document.getElementById('apellidoMaterno').value
    if (apellidoM ==''){
        error.push('Apellido materno')
        confirmacion=1
        
    }

    var edad = document.getElementById('Edad').value
    if (edad ==''){
        error.push('Edad')
        confirmacion=1
        
    }
    if (correo ==''){
        error.push('Correo')
        confirmacion=1
        
            }

    var doc = document.getElementById('nroDoc').value
    if (doc ==''){
        error.push('Numero documento')
        confirmacion=1
        
    }

    var nro = document.getElementById('nroUsuario').value
    if (nro ==''){
        error.push('Numero telefono')
        confirmacion=1
        
    }
    if (confirmacion==1){
        
        alert("Rellene los campos: "+error.join(', '))
    }else{
        alert("LOGRO RELLENAR EL FORMULARIO CORRECTAMENTE WAOS")
    }
    


    }