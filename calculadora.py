from operacoes_factory import OperacaoFactory
from interface_strategy import Soma, Divisao, Subtracao


class Calculadora:
    def realiza_calculo(self, a, b, tipo_de_operacao):
        tipo = OperacaoFactory.get_operacao(tipo_de_operacao)
        valor = tipo.calcula(a, b)
        return valor

#val = Calculadora()
#print(val.realiza_calculo(50, 150, "subtração"))
       