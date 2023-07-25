// nuevo_script.js

// Función para desplazarse (scroll) hasta el formulario
function scrollToForm() {
    const formulario = document.getElementById('formulario');
    formulario.scrollIntoView({ behavior: 'smooth' });
}

// Obtener el botón de enviar del formulario
const botonEnviar = document.getElementById('boton-enviar');

// Agregar un evento clic al botón de enviar para llamar a la función scrollToForm
botonEnviar.addEventListener('click', scrollToForm);