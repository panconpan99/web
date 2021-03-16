var buttonAdd = document.getElementById("add-service");
var servicesCont = document.getElementById("service-cont");
var tbodyEl = document.getElementById("variable");
var services = document.getElementById("service");

buttonAdd.onclick = function() {
    var add = services.value;
    var row = tbodyEl.insertRow(); 
    var cell = row.insertCell(); 
    cell.innerHTML = add;

    if (services.value == "General_Score") {
        description = row.insertCell();
        description.innerHTML = "Texto para general Score";
        value = row.insertCell();
        value.innerHTML = "0,8";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.width = '50';
        inu = row.insertCell();
        inu.appendChild(input);
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
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.width = '50';
        inu = row.insertCell();
        inu.appendChild(input);
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
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.width = '50';
        inu = row.insertCell();
        inu.appendChild(input);
        var image = document.createElement('img');
        image.src = './photos/fans.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "H&E_organo") {
        description = row.insertCell();
        description.innerHTML = "Texto ejemplo para h&e organo";
        value = row.insertCell();
        value.innerHTML = "0,6";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.width = '50';
        inu = row.insertCell();
        inu.appendChild(input);
        var image = document.createElement('img');
        image.src = './photos/he_organo.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "H&E_Alevin") {
        description = row.insertCell();
        description.innerHTML = "Texto h&E alevin";
        value = row.insertCell();
        value.innerHTML = "1,1";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.width = '50';
        inu = row.insertCell();
        inu.appendChild(input);
        var image = document.createElement('img');
        image.src = './photos/he_alevin.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
};
