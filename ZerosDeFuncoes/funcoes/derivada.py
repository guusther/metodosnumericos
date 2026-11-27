#calculo da derivada
from sympy import symbols, diff, lambdify

x = symbols('x')

def calcularDerivada(expressao):
    derivadaSimbolica = diff(expressao, x)
    derivada = lambdify(x, derivadaSimbolica)
    return derivada
