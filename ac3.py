import unittest
from CalculadoraBasica import CalculadoraBasica
from CalculadorAvancada import CalculadorAvancada 

class Testes(unittest.TestCase):
    def test_soma(self):
        calculador = Calculadora()
        result = calculador.calcular(2, 3, 'soma')
        self.assertEqual(result, 5)

    def test_multiplicacao(self):
        calculador = Calculadora()
        result = calculador.calcular(2, 5, 'multiplicacao')
        self.assertEqual(result, 10)

    def test_Divisao(self):
        calculador = Calculadora()
        result = calculador.calcular(2, 4, 'divisao')
        self.assertEqual(result, 0.5)

    def test_subtracao(self):
        calculador = Calculadora()
        result = calculador.calcular(2, 4, 'subtracao')
        self.assertEqual(result, -2)

    def test_subtracao2(self):
        calculador = Calculadora()
        self.assertEqual (calculador.calcular(2, 4, 'subtrair'), 0)
        


if __name__ == '__main__':
    unittest.main()