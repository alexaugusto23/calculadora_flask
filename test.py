import unittest
from app import Operacoes


class MyTestCase(unittest.TestCase):
    def test_fun_soma(self):
        calcula = Operacoes(50, 50)

        test_soma = calcula.soma()
        self.assertEqual(test_soma, 100)
    
    def test_func_multilplicacao(self):
        calcula = Operacoes(50, 50)

        test_mult = calcula.mult()
        self.assertEqual(test_mult, 2501)
    
    def test_tem_valor(self):
        calcula = Operacoes(50, 50)
        self.assertIsNotNone(calcula)


       
if __name__ == '__main__':
    unittest.main()

#python -m unittest teste.py