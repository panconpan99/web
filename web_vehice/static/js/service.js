const buttonAdd = document.getElementById("add-service");
const servicesCont = document.getElementById("service-cont");
const tbodyEl = document.getElementById("variable");
const services = document.querySelector("#service");

buttonAdd.onclick = ()=>{
    const add = services.value;
    const row = tbodyEl.insertRow(); 
    const cell = row.insertCell(); 
    cell.innerHTML = add;
    description = row.insertCell();
    description.innerHTML = "descripcion de prueba";
}