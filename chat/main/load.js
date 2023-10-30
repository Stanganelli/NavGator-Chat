function load() {
    var nome = sessionStorage.getItem("nome")
    nomeDiv.innerHTML = `${nome}`
}

function post() {
    var mensagem = document.getElementById("mensagem").value;
    var nome = sessionStorage.getItem("nome");


    //código demoniaco abaixo
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = xhr.responseText;
            document.getElementById("mensagem").value = "";
            document.getElementById("chat").innerHTML += `<p><strong>${nome}:</strong> ${mensagem}</p>`;
        }
    };

    var data = `user_name=${nome}&mensagem=${mensagem}`;
    xhr.send(data);
}