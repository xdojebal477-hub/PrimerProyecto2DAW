function mostrarResultado(arr) {
    let salida = "";
    const array1 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"];
    for (let dia of array1) {
        salida+=dia+"<br>"
    }
    document.getElementById("salida").innerHTML=salida
}