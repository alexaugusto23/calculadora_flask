import unittest
from calculadora import Calculadora

class MyTestCase(unittest.TestCase):
    def test_fun_soma(self):
        calculator = Calculadora()
        test_soma = calculator.realiza_calculo(50, 50, "soma")
        self.assertEqual(test_soma, 100)
    
    def test_func_divisao(self):
        calculator = Calculadora()
        test_divisao = calculator.realiza_calculo(50, 50, "divisão")
        self.assertEqual(test_divisao, 1)

    def test_func_subtracao(self):
        calculator = Calculadora()
        test_subtracao = calculator.realiza_calculo(50, 50, "subtracao")
        self.assertEqual(test_subtracao, 0)

    def test_func_subtracao_dois(self):
        calculator = Calculadora()
        test_subtracao = calculator.realiza_calculo(100, 99, "subtracao")
        self.assertEqual(test_subtracao, 1)
    
    def test_tem_valor(self):
        calculator = Calculadora()
        calcula = calculator.realiza_calculo(50, 50, "subtracao")
        self.assertIsNotNone(calcula)

       
if __name__ == '__main__':
   log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)
       runner.close()

#python -m unittest teste.py