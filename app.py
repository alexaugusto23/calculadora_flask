from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
from flask import request
import os 

app = Flask(__name__)

#routes
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return '<h1>Óla eu sou uma calculadora</h1>'

@app.route("/soma", methods=['GET', 'POST'])
def soma():
    a = int(request.args.get('valor_a'))
    b = int(request.args.get('valor_b'))

    valor = Operacoes.soma(a,b)

    return str(valor)

class Operacoes():

    def soma(a,b):
        return a+b

    def subtracao(a,b):
        return a-b
    
    def multiplicacao(a,b):
        return a*b
    
    def divisao(a,b):
        return a/b

    def divisao_interia(a,b):
        return a//b
    
    def resto(a,b):
        return a%b 
    
    def potencia(a,b):
        return a**b 
        

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
