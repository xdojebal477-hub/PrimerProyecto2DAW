function ordenarNum(arr) {
    let pares = [];
    let impares = [];

    // Clasificación
    for (let num of arr) {
      if (num % 2 === 0) {
        pares.push(num);
      } else {
        impares.push(num);
      }
    }

    // Ordenamos fuera del bucle
    pares.sort((a, b) => a - b);
    impares.sort((a, b) => a - b);

    // Si el array original tiene longitud impar → impares primero
    if (arr.length % 2 !== 0) {
      return [...impares, ...pares];
    } else {
      return [...pares, ...impares];
    }
  }

  function mostrarResultado() {
    const array1 = [9, 4, 6, 5, 3, 2, 1, 8, 7];
    const resultado = ordenarNum(array1);
    document.getElementById("resultado").innerHTML = 
      `Resultado: [${resultado.join(', ')}]`;
  }