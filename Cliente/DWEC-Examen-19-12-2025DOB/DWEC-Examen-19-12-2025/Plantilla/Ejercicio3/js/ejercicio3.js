const formulario=document.forms['formularioStock'];
const fabricanteInput=formulario.fabricante;
const productoInput=formulario.producto;
const fechaInput=formulario.fecha;
const referenciaInput=formulario.referencia;
const ubicacionInput=formulario.ubicacion;
const categoriaSelect=formulario.elements['categoria']
const mensajes=document.querySelector("#mensajes")

formulario.addEventListener('submit',(e)=>{
    
    let categoria=categoriaSelect.value;
    
    let fabricante=fabricanteInput.value;
    let producto=productoInput.value;
    let fecha=fechaInput.value;
    let referencia=referenciaInput.value;
    let ubicacion=ubicacionInput.value;
    

    



    let vacios=[];
    
    let errores=[];
    
    if(!categoria ){
        vacios.push("Debe seleccionar una categoria");
        let categoriaDiv=document.createElement('div');
        categoriaDiv.textContent="Debe seleccionar una categoria";
        categoriaDiv.classList.add("empty-list");
        mensajes.appendChild(categoriaDiv);
    }
    



    if(fabricante.trim()===""){
        vacios.push("Fabricante no puede ser vacio");
        let fabricanteDiv=document.createElement('div');
        fabricanteDiv.textContent="Fabricante no puede ser vacio";
        fabricanteDiv.classList.add("empty-list");
        mensajes.appendChild(fabricanteDiv);
    }
    if(/^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/.test(fabricante)){
        console.log("categoria valida");
    }
    else{
        errores.push("Fabricante invalido");
        let fabricanteDivError=document.createElement('div');
        fabricanteDivError.textContent="Fabricante invalido";
        fabricanteDivError.classList.add("error-list");
        mensajes.appendChild(fabricanteDivError);
    }




    if(producto.trim()===""){
        vacios.push("producto no puede ser vacio");
        let productoDiv=document.createElement('div');
        productoDiv.textContent="producto no puede ser vacio";
        productoDiv.classList.add("empty-list");
        mensajes.appendChild(productoDiv);
    }
    if(/^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/.test(fabricante)){
        console.log("producto valido");
    }
    else{
        errores.push("Producto invalido");
        let productoDivError=document.createElement('div');
        productoDivError.textContent="producto invalido";
        productoDivError.classList.add("error-list");
        mensajes.appendChild(productoDivError);
    }




    if(fecha.trim()===""){
        vacios.push("fecha no puede ser vacio");
        let fechaDiv=document.createElement('div');
        fechaDiv.textContent="fecha no puede ser vacio";
        fechaDiv.classList.add("empty-list");
        mensajes.appendChild(fechaDiv);
    }
    if(/^\d{2}\/\d{2}\/\d{4}$/.test(fecha)){
        console.log("fecha valida");
    }
    else{
        let fechaDivError=document.createElement('div');
        fechaDivError.textContent="fecha invalido";
        fechaDivError.classList.add("error-list");
        mensajes.appendChild(fechaDivError);
    }



    if(referencia.trim()===""){
        vacios.push("referencia no puede ser vacio");
        let referenciaDiv=document.createElement('div');
        referenciaDiv.textContent="referencia no puede ser vacio";
        referenciaDiv.classList.add("empty-list");
        mensajes.appendChild(referenciaDiv);

    }
    if(ubicacion.trim()===""){
        vacios.push("ubicacion no puede ser vacio");
        let ubicacionDiv=document.createElement('div');
        ubicacionDiv.textContent="ubicacion no puede ser vacio";
        ubicacionDiv.classList.add("empty-list");
        mensajes.appendChild(ubicacionDiv);
    }
    if(/^[A-Z]\-^d{2}[0-99]/.test(ubicacion)){
        console.log("ubi correcta");
        
    }
    
    else{
        let ubicacionDivError=document.createElement('div');
        ubicacionDivError.textContent="ubicacion invalido";
        ubicacionDivError.classList.add("error-list");
        mensajes.appendChild(ubicacion);
    }//cuando comprueba la ubicacion salta directamente hasta el siguiente html 
    




    if(vacios.length>0 || errores.length>0){
        e.preventDefault();
        alert(vacios.join("\n"));
        alert(errores.join("\n"));        
    }
    else{
        alert("Formulario sin vacios");
        alert("Valores correctos")
    }
}); 