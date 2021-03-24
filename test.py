import unittest
from libro import Libro
from examen import Examen
from autor import Autor

class Pruebas(unittest.TestCase):

    def test_mas_antiguos(self):
        libro1 = Libro(autor = "Pepe", titulo = "Memorias", anyo = 1866)
        libro2 = Libro(autor = "Pepe", titulo = "Memorias 2", anyo = 1969)
        libro3 = Libro(autor = "Pepe", titulo = "Memorias 3", anyo = 2022)
        
        self.assertIsInstance(libro1, Libro)
        self.assertIsInstance(libro2, Libro)
        self.assertIsInstance(libro3, Libro)

class Suite(unittest.TestSuite):
    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_mas_antiguos'))
        
if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)