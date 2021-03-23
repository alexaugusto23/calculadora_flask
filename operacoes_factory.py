from interface_strategy import Multiplicacao, Soma, Divisao, Subtracao

class OperacaoFactory():

    @staticmethod
    def get_operacao(tipo_operacao):
        try:
            if tipo_operacao.lower() == "divisão" or tipo_operacao.lower() == "divisao":
                return Divisao()
            elif tipo_operacao.lower() == "soma":
                return Soma()
            elif tipo_operacao.lower() == "subtração" or tipo_operacao.lower() == "subtracao":
                return Subtracao()
            elif tipo_operacao.lower() == "multiplicação" or tipo_operacao.lower() == "multiplicacao":
                return Multiplicacao()
            raise AssertionError ("Operação não econtrada") 
        except AssertionError as erro:
            print(erro)

#tipo = OperacaoFactory.get_operacao("soma")
#valor = tipo.calcula(10,20)
#print(valor)