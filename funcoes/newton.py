from sympy import symbols
from sympy import diff
from sympy import lambdify
from derivada import calcularDerivada

x = symbols('x')

def funcao(x):
    return x**3 - x - 2

def newton(x0, funcao, tolerancia):
    i = 1
    historico = []
    derfx0 = calcularDerivada(x**3 - x - 2)
    while True:
        print(f"Iteração {i}")
        
        fx0 = funcao(x0)
        derfx0arm = derfx0(x0)

        print(f"x atual: {x0}")
        print(f"f(x0): {fx0}")
        print(f"f'(x0): {derfx0arm}")

        x1 = x0 - (fx0 / derfx0arm)
        if abs(funcao(x1)) < tolerancia:
            break
        else:
            x0 = x1
        historico.append({"iteração": i, "x": x0, "fx": fx0, "f'x": derfx0arm})
        print("==========================================")
    return historico

        
