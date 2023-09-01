from ohce.ohcekata import OhceKata
import unittest

class TestOhceKata(unittest.TestCase):
    def test_saludo(self):
        kata = OhceKata("Gustavo")
        self.assertEqual(kata.saludo(), "¡Buenas tardes Gustavo!")
