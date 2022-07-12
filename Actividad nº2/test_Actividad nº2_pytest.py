import pytest
import actividad2

def test_factorial():
   assert actividad2.factorial(4) == 24

def test_primo():
   assert actividad2.primo(5) == True
   assert actividad2.primo(10) == False

def test_multiplicacion():
   assert actividad2.multiplicacion(10,2) == 20
   assert actividad2.multiplicacion(11,3) == 33

def test_enteros():
   assert actividad2.enteros(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_area_triangulo():
   assert actividad2.area_triangulo(2,4) == 4