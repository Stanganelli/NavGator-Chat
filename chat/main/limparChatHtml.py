#pelo visto vamo passar parametro por aqui
file_html = open("chat.html", "w")
file_html.write('''
<!DOCTYPE html>
<html>

<head>
    <script src="load.js"></script>
    <title>Chat</title>
    <style>
        #chat {
            width: 300px;
            height: 400px;
            border: 1px solid #000;
            padding: 10px;
            overflow-y: scroll;
        }
    </style>
</head>

<body>
    <center>
    <div id="chat"></div>
    <span type="text" id="nomeDiv" placeholder="Seu nome"></span>
    <input type="text" id="mensagem" placeholder="Digite uma mensagem">
    <button onclick="post()">Enviar</button>
    </center>
</body>

<script>
    nome = ""
    load()

    
</script>

</html>
''')
file_html.close()
