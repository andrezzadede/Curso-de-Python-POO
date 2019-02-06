# TDD test drive develop basicamente ele rafaz as classes, passasando os testes, e melhorando sempre que possivel

import unittest
from calculadora import Calculadora


class TddExemplo(unittest.TestCase):

    def teste_soma(self):
        calc = Calculadora()
        result = calc.somar(-20, 40)
        self.assertEqual(20, result
    
    def test_sub(self):
        calc = Calculadora()
        result = cal.subtrair(40,20)
        self.assertEqual(20, result)


if __name__ == '__name__':
    print(unittest.main())