
const listarPacientes_h = async (id_hosp) => {
    try {

        const response = await fetch (`/pacientes_h/${id_hosp}`);
        const data = await response.json();

        let tabla = ``;
        data.data.forEach((i) => {
        
            tabla += `<tr>`
            tabla += `<td>${i.run}</td>`;
            tabla += `<td>${i.nombre} ${i.ape_pat} ${i.ape_mat}</td>`;
            tabla += `<td>${i.fecha_def}</td>`;
            tabla += '</tr>';

        });
        
        defuncionesTableBody.innerHTML = tabla;

        
    } catch (error) {
        console.log(error);
    }
};

const listarPacientes_r = async (id_reg) => {
    try {

        const response = await fetch (`/pacientes_r/${id_reg}`);
        const data = await response.json();

        let tabla = ``;
        data.data.forEach((i) => {
        
            tabla += `<tr>`
            tabla += `<td>${i.run}</td>`;
            tabla += `<td>${i.nombre} ${i.ape_pat} ${i.ape_mat}</td>`;
            tabla += `<td>${i.fecha_def}</td>`;
            tabla += '</tr>';

        });
        
        defuncionesTableBody.innerHTML = tabla;

        
    } catch (error) {
        console.log(error);
    }
};



window.addEventListener("load", async () => {
    

    hospitalSelect.addEventListener("change", (event) => { 
        listarPacientes_h(event.target.value);
    });
    
    regionSelect.addEventListener("change", (event) => {
        listarPacientes_r(event.target.value);
    });
    
});