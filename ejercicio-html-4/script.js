const numero = document.getElementById("numero");
const botonSumar = document.getElementById("boton-sumar");
const botonRestar = document.getElementById("boton-restar");

let contador = 0;

botonSumar.addEventListener("click", function () {
    contador++;
    numero.textContent = contador;
});

botonRestar.addEventListener("click", function () {
    contador--;
    numero.textContent = contador;
});