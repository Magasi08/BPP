# funciones.py

"""Contiene diversas funciones matemáticas.

Este módulo permite al usuario realizar diferentes operaciones matemáticas.

El módulo contiene las siguientes funciones:

- `factorial(numero)` - Función que devuelve el factorial de un número.
- `primo(num)` - Función que devuelve si un número es primo o no.
- `multiplicacion(val1, val2)` - Función que multiplica dos argumentos numéricos recibidos entre ellos.
- `enteros(n)` - Función que devuelve los valores enteros entre 0 y el número ingresado.
- `area_triangulo(base, altura)` - Función que devuelve el área de un triángulo.
"""

def factorial(numero):
    """Función que devuelve el factorial de un número.

    Examples:
        >>> factorial(4)
        24
        
    Args:
        numero (int): valor cuyo factorial se desea calcular.
        
    Returns:
        factorial (int): Un número que representa el factorial de `numero`.
    """
    factorial = 1
    for n in range(1,numero+1):
       factorial = factorial * n
    return factorial

def primo(num):
    """Función que devuelve si un número es primo o no.

    Examples:
        >>> primo(5)
        True
        
    Args:
        num (int): número a determinar si es o no primo.
        
    Returns:
       Value (bool): Indica si el número es primo o no.
    """
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True



def multiplicacion(val1, val2=1):
    """Función que multiplica dos argumentos numéricos recibidos entre ellos.

    Examples:
        >>> multiplicacion(4.0, 2.0)
        8.0
        >>> multiplicacion(4, 2)
        8

    Args:
        val1 (int o float): un número que es uno de los factores a multiplicar.
        val2 (int o float): un número que es uno de los factores a multiplicar.
    
    Raises:
            Exception: devuelve una excepción si los valores ingresados no son tipo float o int.
    
    Returns:
       Producto (int o float): Un número que representa el producto de `val1` y `val2`.
    """
    try:
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            producto=val1*val2
            return producto
        else:
            raise Exception("Todos los argumentos recibidos deben ser valores numéricos")
    except Exception as error:
        print(error)



def enteros(n):
    """Función que devuelve los valores enteros entre 0 y el número ingresado

    Args:
        n (int): número para el cual se quiere encontrar los números enteros entre éste y 0.

    Returns:
        numeros (lista): lista de números enteros encontrados entre 0 y el número ingresado.
    """
    numeros=[]
    for i in range(int(n)+1):
        numeros.append(i)
    return numeros



def area_triangulo(base, altura):
    """Función que devuelve el área de un triángulo

    Args:
        base (int o float): valor que representa la base de un triángulo.
        altura (int o float): valor que representa la altura de un triángulo.

    Raises:
        Exception: devuelve una excepción si los valores ingresados no son tipo float o int.

    Returns:
        area (int o float): Es el valor del área del triángulo.
    """

    try:
        if isinstance(base, (int, float)) and isinstance(altura, (int, float)):
            area=base*altura/2
            return area
        else:
            raise Exception("Todos los valores recibidos deben ser valores numéricos")
    except Exception as error:
        print(error)

