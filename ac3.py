import unittest
from CalculadoraBasica import CalculadoraBasica
from CalculadorAvancada import CalculadorAvancada 

class MyTestCase(unittest.TestCase):
    def tes_something(self):
        calcula = CalculadoraBasica()
        testesoma = calcula.somar(5, 4)
        self.assertEqual(testesoma, 9)

        testesoma = calcula.dividir(5,4)
        self.assetEqual(testesoma, 1.25)


    def teste_avancado(self):
        calculaAvanc = CalculadorAvancada()
        testeRais= calculaAvanc.raizQuadrada(81)
        self.assertEqual(testeRaiz, 9)


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