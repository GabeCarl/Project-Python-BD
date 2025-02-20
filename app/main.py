"""API python com flask."""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Função para retorna uma string na rota / da API."""
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
