import unittest
import actividad2

class Testactividad2(unittest.TestCase):
   def test_factorial(self):
         resultado = actividad2.factorial(4)
         self.assertEqual(resultado,24)

   def test_primo(self):
         resultado = actividad2.primo(10)
         self.assertFalse(resultado)
         resultado = actividad2.primo(5)
         self.assertTrue(resultado)

   def test_multiplicacion(self):
      resultado = actividad2.multiplicacion(10,2)
      self.assertEqual(resultado,20)
      resultado = actividad2.multiplicacion(11,3)
      self.assertEqual(resultado,33)

   def test_enteros(self):
      resultado = actividad2.enteros(10)
      self.assertEqual(resultado,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   
   def test_area_triangulo(self):
      resultado = actividad2.area_triangulo(3,4)
      self.assertEqual(resultado,6)

if __name__ == '__main__':
    unittest.main()