from ohce.ohcekata import OhceKata
import unittest

class TestOhceKata(unittest.TestCase):
    def test_saludo(self):
        kata = OhceKata("Gustavo")
        self.assertEqual(kata.saludo(), "¡Buenas tardes Gustavo!")

    def test_invertir_palabra(self):
        kata = OhceKata("Esteban")
        self.assertEqual(kata.invertir_palabra("santiago"),"ogaitnas")    
