const inputTarea = document.getElementById("input-tarea");
const botonAgregar = document.getElementById("boton-agregar");
const listaTareas = document.getElementById("lista-tareas");

botonAgregar.addEventListener("click", function () {
    const textoTarea = inputTarea.value.trim();

    if (textoTarea === "") {
        return;
    }

    const nuevaTarea = document.createElement("li");
    nuevaTarea.textContent = textoTarea;

    nuevaTarea.addEventListener("click", function () {
        nuevaTarea.remove();
    });

    listaTareas.appendChild(nuevaTarea);
    inputTarea.value = "";
});