from flask import Flask, request, render_template

app = Flask(__name__)

# Simula um "banco de dados" (dicionário)
usuarios = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form['nome']
    senha = request.form['senha']

    # Armazena os dados (apenas demonstração)
    usuarios[nome] = senha

    return f"<h2>Usuário {nome} cadastrado com sucesso!</h2><br><a href='/'>Voltar</a>"

if __name__ == '__main__':
    app.run(debug=True)
