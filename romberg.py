
import sympy as sp
from sympy.abc import x

def funcion(ecua='x+2'):
    return sp.sympify(ecua)
  
def romberg(f, a, b, eps = 1E-8):
  # Romberg en R[0,0]
    R = [[0]] 
    print(R[0])
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])
        R[n][0] = 0.5*R[n-1][0] + h*sum(f.evalf(subs={x:(a+(2*k-1)*h)}) for k in range(1, 2**(n-1)+1)) 
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print(R[n])
        if abs(R[n][n-1] - R[n][n]) < eps:
            print("Conseguido en n: ", n," iteraciones con error : ",abs(R[n][n-1] - R[n][n]))
            return R[n][n]
        n += 1

#iniamos el programa con lo siguiente parametros
f=funcion(input("Introduzca f: "))
a=float(input("Introduzca a: "))
b=float(input("Introduzca b: "))
eps=float(input("Introduzca el error: "))
r=romberg(f,a,b,eps)
print (r)




