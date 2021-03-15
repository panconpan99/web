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
        image.width = "200";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "service1") {
        description = row.insertCell();
        description.innerHTML = "Description for Service 1";
        value = row.insertCell();
        value.innerHTML = "2";
        var image = document.createElement('img');
        image.src = 'test.jpg';
        image.width = "200";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "service2") {
        description = row.insertCell();
        description.innerHTML = "Description for Service 2";
        value = row.insertCell();
        value.innerHTML = "0.01";
        var image = document.createElement('img');
        image.src = 'test.jpg';
        image.width = "200";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
    if (services.value == "service3") {
        description = row.insertCell();
        description.innerHTML = "Description for Service 3";
        value = row.insertCell();
        value.innerHTML = "1000";
        var image = document.createElement('img');
        image.src = 'test.jpg';
        image.width = "200";
        ige = row.insertCell(); 
        ige.appendChild(image);
    }
};
