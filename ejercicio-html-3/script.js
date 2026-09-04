const formulario = document.getElementById("formulario");
const inputNombre = document.getElementById("nombre");
const inputEmail = document.getElementById("email");
const mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    const nombre = inputNombre.value.trim();
    const email = inputEmail.value.trim();

    if (nombre === "" || email === "") {
        mensaje.textContent = "completa todos los datos !!!";
        mensaje.className = "error";
        return;
    }

    mensaje.textContent = `perfecto ${nombre} recibimos tus datos! nos comunicaremos a ${email}.`;
    mensaje.className = "exito";
});