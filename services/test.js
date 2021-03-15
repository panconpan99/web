var buttonAdd = document.getElementById("add-service");
var servicesCont = document.getElementById("service-cont");
var tbodyEl = document.getElementById("variable");
var services = document.getElementById("service");

buttonAdd.onclick = function() {
    var add = services.value;
    var row = tbodyEl.insertRow(); 
    var cell = row.insertCell(); 
    cell.innerHTML = add;
    if (services.value == "service0") {
        description = row.insertCell();
        description.innerHTML = "Description for Service 0";
        value = row.insertCell();
        value.innerHTML = "30";
        var image = document.createElement('img');
        image.src = 'test.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "General_Score") {
        description = row.insertCell();
        description.innerHTML = "Texto para general Score";
        value = row.insertCell();
        value.innerHTML = "0,8";
        var image = document.createElement('img');
        image.src = './photos/general.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "Score_Gill") {
        description = row.insertCell();
        description.innerHTML = "Texto ejemplo para Score Gill";
        value = row.insertCell();
        value.innerHTML = "0,5";
        var image = document.createElement('img');
        image.src = './photos/gill.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "Detección_de_FANs") {
        description = row.insertCell();
        description.innerHTML = "Texto para la deteccion de fans";
        value = row.insertCell();
        value.innerHTML = "0,42";
        var image = document.createElement('img');
        image.src = './photos/fans.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
};
