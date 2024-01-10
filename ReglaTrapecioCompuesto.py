"""Daniel Nino-Regla Trapecio Compuesto"""
"""imports"""
from sympy.abc import x
from sympy import sympify, lambdify, integrate
from pyreadline3 import Readline
readline = Readline()
"""Funcion que permite recibir como valor numero pi o e"""
def my_float(s):
    constants = {"pi": 3.14159, "e": 2.71928}
    if s in constants:
        return constants[s]
    else:
        return float(s)
"""Funcion que realiza la integral del trapecio"""
"""parametros funcion, cantidad de interaciones, a y b"""
def trapecio(f, n, a, b):
    """calcular la funcion en a y en b y sumarla"""
    integral = f(a) + f(b)
    """calcular el h"""
    h = (b-a)/n
    """ciclo para sumar los demas reemplazos"""
    for i in range(1, n):
        """calcular la x"""
        x=a+i*h
        """sumarlo a la integral"""
        integral += 2*f(x)
        """retornar el resultado final"""
    return ((h)*integral)*1/2
"""main"""
def main():
    """ingreso de datos"""
    string = input("Ingrese la Función: ")
    """configurar la funcion"""
    f = sympify(string)
    f = lambdify(x, f)
    n = int(input("Ingrese N: "))
    """a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))"""
    a = my_float(input("Ingrese a: "))
    b = my_float(input("Ingrese b: "))
    """calcular la integral"""
    integral = trapecio(f,n,a,b)
    """calculo del error restando con la integral real de la formula"""
    IntegralRe=integrate(string, (x, a, b))
    Error=abs(IntegralRe-integral)
    """imprimir resultados"""
    print(f"Integral por trapecio es {string}, de {a} a {b} es aprox: {integral}")
    print(f"Integral de {string}, de {a} a {b} es: {IntegralRe}")
    print(f"Tiene error de {Error}")
if __name__ == '__main__':
    main()
