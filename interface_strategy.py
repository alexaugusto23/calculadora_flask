from abc import ABCMeta, abstractstaticmethod


class Operacao(metaclass = ABCMeta):

    @abstractstaticmethod
    def calcula(self, a,b):
        pass
        """ Interface Implementa classes filhas """

class Divisao(Operacao):
    def calcula(self, a,b):
        return a / b

class Soma(Operacao):
    def calcula(self, a,b):
        return a + b

class Subtracao(Operacao):
    def calcula(self, a,b):
        return a - b

class Multiplicacao(Operacao):
    def calcula(self, a,b):
        return a * b