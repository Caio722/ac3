import unittest
import ac3_cal


class MyTestCase(unittest.TestCase):
    def test_soma(self):
        calculador = ac3_cal.Calculadora()
        result = calculador.calcular(2, 3, 'soma')
        self.assertEqual(result, 5)

    def test_multiplicacao(self):
        calculador = ac3_cal.Calculadora()
        result = calculador.calcular(2, 5, 'multiplicacao')
        self.assertEqual(result, 10)

    def test_Divisao(self):
        calculador = ac3_cal.Calculadora()
        result = calculador.calcular(2, 4, 'divisao')
        self.assertEqual(result, 0.5)

    def test_subtracao(self):
        calculador = ac3_cal.Calculadora()
        result = calculador.calcular(2, 4, 'subtracao')
        self.assertEqual(result, -2)

    def test_potencicao(self):
        calculador = ac3_cal.Calculadora()
        self.assertEqual(calculador.calcular(2, 4, 'potenciacao'), 0)


if __name__ == '__main__':
    unittest.main()
