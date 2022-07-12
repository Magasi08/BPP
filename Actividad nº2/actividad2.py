def factorial(numero):
    '''Función que devuelve el factorial de un número'''
    factorial = 1
    for n in range(1,numero+1):
       factorial = factorial * n
    return factorial



def primo(num):
    '''Función que devuelve si un número es primo o no'''
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
    '''Función que multiplica dos argumentos numéricos recibidos entre ellos'''
    try:
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            producto=val1*val2
            return producto
        else:
            raise Exception("Todos los argumentos recibidos deben ser valores numéricos")
    except Exception as error:
        print(error)



def enteros(n):
    '''Función que devuelve los valores enteros entre 0 y el número ingresado'''
    numeros=[]
    for i in range(int(n)+1):
        numeros.append(i)
    return numeros



def area_triangulo(base, altura):
    '''Función que devuelve el área de un triángulo'''
    try:
        if isinstance(base, (int, float)) and isinstance(altura, (int, float)):
            area=base*altura/2
            return area
        else:
            raise Exception("Todos los valores recibidos deben ser valores numéricos")
    except Exception as error:
        print(error)

