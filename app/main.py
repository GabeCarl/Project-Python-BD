"""API python com flask."""

# Importa bibliotecas importante para API como request para requisições e jsonify para converter os dados em json
from flask import Flask, request, jsonify

# Importa biblioteca do Banco de dados
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cria a rota /
@app.route("/")
def hello_world():
    """Função para retorna uma string na rota / da API."""
    return "<p>Hello, World!</p>"

# Cria a rota test que 
@app.route('/test', methods=['GET'])
def getTest():
    name = request.args.get('name', 'Gabriel')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
