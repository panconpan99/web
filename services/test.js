var buttonAdd = document.getElementById("add-service");
var servicesCont = document.getElementById("service-cont");
var tbodyEl = document.getElementById("variable");
var services = document.getElementById("service");

buttonAdd.onclick = function() {
    var add = services.value;
    var row = tbodyEl.insertRow(); 
    var cell = row.insertCell(); 
    cell.innerHTML = add;
};
