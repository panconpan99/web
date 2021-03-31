$(document).ready(function(){
    $("#add-service").on("click",crear);
    function crear(){
        const id = $("#service").val();
        $.ajax({
            data: {'serv':id},
            url: '/index/',
            type: 'GET',
            data: 'json',
            success:function(){
                alert("ingresando valores");
            }
        })
    }
})

/*.onclick = ()=>{
    
    const add = services.value;
    ajax({
        data: {'serv':add},
        url: '/app_1/index.html',
        type: 'get',
    })

    const row = tbodyEl.insertRow(); 
    const cell = row.insertCell(); 
    cell.innerHTML = add;
    description = row.insertCell();
    description.innerHTML = "descripcion de prueba";
}*/