let cadena = prompt("Introduce una cadena de texto:");
let cadenaFinal=cadena.trim();
document.getElementById("resultado").innerHTML = "Tu nombre y apellidos mide "+ cadenaFinal.length + " caracteres.";
document.getElementById("resultado2").innerHTML = "Tu nombre y apellidos en mayúsculas es: "+ cadenaFinal.toUpperCase() + ".";
document.getElementById("resultado2").innerHTML = "Tu nombre y apellidos en minisculas  es: "+ cadenaFinal.toLowerCase + ".";