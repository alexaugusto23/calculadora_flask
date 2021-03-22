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
    msg = "<h1>Digite na URL (/index/seu nome aqui) para iniciar a calculadora.</h1>"
    return msg

@app.route("/index/<string:nome>", methods=['GET', 'POST'])
def index(nome = None):
    msg = f"<h1>Olá {nome}, seja bem vindo a calculadora!</h1>\n<h3>Digite na URL (/operacoes/valor(ex 10)/valor(ex 30)/operação(ex soma)</h3>"
    return msg

@app.route("/operacoes/<int:a>/<int:b>/<string:c>", methods=['GET'])
def operacoes(a, b, c):
    lista = [] 
    print(c)
    #a = int(request.args.get('a')) # usar quando passar valor se <> somente? a=valor 
    #b = int(request.args.get('b'))
    #operacoes = request.args.get('operacao')

    valor = Operacoes(a, b)
    if c.lower() == 'soma':
        resultado_um = f"<h1>{str(valor.soma())}</h1>"
        lista.append(resultado_um)
    else:
        resultado_nao_econtrado = f"<h1>Operação não econtrada</h1>"
        lista.append(resultado_nao_econtrado)

    
    #resultado_dois = f"<h1>{str(valor.mult())}</h1>"
    
    #lista.append(resultado_dois)
    print(lista)

    return f"Soma: {lista[0]}"



class Operacoes:
    def __init__ (self, a, b):
        self.a = a
        self.b = b


    def soma(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b    


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)