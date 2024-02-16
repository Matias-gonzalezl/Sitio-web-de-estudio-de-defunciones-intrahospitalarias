
// **** Validaciones login end ****

// **** Validaciones recomendaciones start ****

// Función para habilitar o deshabilitar el select correspondiente
function toggleSelect() {
  const radios = document.getElementsByName("nivel");

  for (let i = 0; i < radios.length; i++) {
    const radio = radios[i];
    const selectId = radio.getAttribute("data-select-id");
    const select = document.getElementById(selectId);

    if (radio.checked) {
      select.removeAttribute("disabled");
    } else {
      select.setAttribute("disabled", "true");
    }
  }
}

// Lista de recomendaciones
const recomendaciones = [
  "Mejorar la calidad de la atención médica: Asegurarse de que los hospitales públicos brinden atención médica de alta calidad es fundamental. Esto incluye contar con personal médico y de enfermería bien capacitado, instalaciones y equipos actualizados, y seguir prácticas clínicas basadas en evidencia. Realizar auditorías de calidad y revisiones periódicas para identificar áreas de mejora y abordarlas.",
  "Enfoque en la prevención: Promover una atención médica preventiva sólida puede ayudar a evitar enfermedades y afecciones que puedan llevar a la hospitalización. Esto incluye campañas de vacunación, detección temprana de enfermedades, educación sobre la salud y promoción de estilos de vida saludables.",
  "Mejorar la gestión de recursos: Gestionar eficazmente los recursos, como camas de hospital, personal médico y suministros, es crucial para evitar defunciones innecesarias. La asignación eficiente de recursos puede ayudar a garantizar que todos los pacientes reciban la atención que necesitan a tiempo.",
  "Educación del paciente y participación: Fomentar la educación del paciente sobre su propia salud y tratamiento puede empoderar a las personas para tomar decisiones informadas y seguir el tratamiento de manera adecuada. Además, involucrar a los pacientes en su atención médica y escuchar sus preocupaciones puede llevar a mejores resultados.",
  "Coordinación de la atención: La coordinación de la atención entre diferentes departamentos, especialistas y niveles de atención médica es esencial. Asegurarse de que la información del paciente se comparta de manera efectiva entre los proveedores de atención y que los pacientes sean derivados a especialistas cuando sea necesario puede evitar complicaciones graves.",
];

// Función para generar una recomendación al azar
function generarRecomendacionAzar() {
  // Obtener una recomendación al azar de la lista
  const recomendacion =
    recomendaciones[Math.floor(Math.random() * recomendaciones.length)];

  // Mostrar la recomendación en la página
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.style.display = "block";
  resultadoDiv.textContent = recomendacion;
}

// Manejar el clic en el botón "Generar recomendación"
document
  .getElementById("generarRecomendacion")
  .addEventListener("click", generarRecomendacionAzar);

// **** Validaciones recomendaciones end ****
