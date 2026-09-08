from sympy import symbols
from sympy import diff
from sympy import lambdify
from .derivada import calcularDerivada

x = symbols('x')

def newton(x0, funcao, tolerancia):
    
    historico = []
    derfx0 = calcularDerivada(x**3 - x - 2)
    while True:
        i = len(historico) + 1
        
        fx0 = funcao(x0)
        derfx0arm = derfx0(x0)
        if derfx0arm == 0:
            raise ValueError(f"Derivada zero em x = {x0}, método de Newton não pode continuar.")

        x1 = x0 - (fx0 / derfx0arm)
        historico.append({"iteração": i, "x": x1, "fx": funcao(x1), "f'x": derfx0arm})
        if abs(funcao(x1)) < tolerancia:
            break
        else:
            x0 = x1
    return historico

        
