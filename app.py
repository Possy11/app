from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def home2():
    nome = request.form['nome']
    return "O nome enviado é:" + nome



@app.route("/home")
def home():
    return '''<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formulário de Cadastro</title>
</head>
<body>

<h2>Formulário de Cadastro</h2>

<form action="/register" method="post">
    <label for="nome">Nome:</label><br>
    <input type="text" id="nome" name="nome" placeholder="NOMEZINHO" required><br><br>
    
    <label for="cpf">CPF DA PEOPLE:</label><br>
    <input type="text" id="cpf" name="cpf" pattern="\d{3}\.\d{3}\.\d{3}-\d{2}" placeholder="CPF" required><br><br>
    
    <input type="submit" value="Enviar">
    <a href="/register">link text</a>
</form>

</body>
</html>'''