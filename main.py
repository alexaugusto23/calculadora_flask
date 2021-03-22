from calculadora import Calculadora
from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
from flask import request 
from flask import jsonify
from flask import abort
import os 

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):

    return "<style>h1 {text-align: center;}</style><h1>Esse endereço de URL não existe!</h1>", 404

#routes
@app.route("/")
def raiz():
    return render_template("index.html")

@app.route("/index/<string:nome>", methods=['GET', 'POST'])
def index(nome = None):
    return render_template("home.html", msg = nome)

@app.route("/operacoes/<int:a>/<int:b>/<string:operacao>", methods=['GET'])
def operacoes(a, b, operacao):
    calculator = Calculadora()
    valor = calculator.realiza_calculo(a, b, operacao)
    return render_template("calculadora.html", operacao=operacao, a=a, b=b, valor=valor)

@app.route("/teste", methods=['GET'])
def teste():
    get_path_atual = os.getcwd()
    os.chdir(get_path_atual)
    resultado_scripty = os.system("py test.py")
    #print(resultado_scripty)

    return render_template("teste.html", valor = resultado_scripty)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)