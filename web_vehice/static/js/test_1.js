var buttonAdd = document.getElementById("add-service");
var servicesCont = document.getElementById("service-cont");
var tbodyEl = document.getElementById("variable");
var services = document.getElementById("service");

buttonAdd.onclick = function() {
    var add = services.value;
    var row = tbodyEl.insertRow(); 
    var cell = row.insertCell(); 
    cell.innerHTML = add;

    if (services.value == "General Score") {
        description = row.insertCell();
        description.innerHTML = "Texto para general Score";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.setAttribute("value", "1");
        input.min=1;
        inu = row.insertCell();
        inu.appendChild(input);
        value = row.insertCell();
        value.innerHTML = input.valueAsNumber * 0.8;
        input.width = '50';
        var image = document.createElement('img');
        image.src = '../photos/general.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "Score Gill") {
        description = row.insertCell();
        description.innerHTML = "Texto ejemplo para Score Gill";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.setAttribute("value", "1");
        input.min=1;
        inu = row.insertCell();
        inu.appendChild(input);
        value = row.insertCell();
        value.innerHTML = input.valueAsNumber * 0.5;
        input.width = '50';
        var image = document.createElement('img');
        image.src = '../photos/gill.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "Detección de FANs") {
        description = row.insertCell();
        description.innerHTML = "Texto para la deteccion de fans";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.setAttribute("value", "1");
        input.min=1;
        inu = row.insertCell();
        inu.appendChild(input);
        value = row.insertCell();
        value.innerHTML = input.valueAsNumber * 0.42;
        input.width = '50';
        var image = document.createElement('img');
        image.src = '../photos/fans.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "H&E organo") {
        description = row.insertCell();
        description.innerHTML = "Texto ejemplo para h&e organo";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.setAttribute("value", "1");
        input.min=1;
        inu = row.insertCell();
        inu.appendChild(input);
        value = row.insertCell();
        value.innerHTML = input.valueAsNumber * 0.6;
        input.width = '50';
        var image = document.createElement('img');
        image.src = '../photos/he_organo.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "H&E Alevin") {
        description = row.insertCell();
        description.innerHTML = "Texto h&E alevin";
        var input = document.createElement('input');
        input.setAttribute("type", "number");
        input.setAttribute("value", "1");
        input.min=1;
        inu = row.insertCell();
        inu.appendChild(input);
        value = row.insertCell();
        value.innerHTML = input.valueAsNumber * 1.1;
        input.width = '50';
        var image = document.createElement('img');
        image.src = '../photos/he_alevin.jpg';
        image.width = "100";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
};
