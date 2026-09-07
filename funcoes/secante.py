from sympy import symbols
from sympy import diff
from sympy import lambdify


def secante(x0, x1,funcao, tolerancia):
     
     historico = []
     while True:
        i = len(historico) + 1
        print(f"Iteração {i}:")
        
        print(f"x0 e x1 atuais: {x0} e {x1}")
        fx1 = funcao(x1)
        fx0 = funcao(x0)
        x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        fx2 = funcao(x2)
        print(f"x2 atual: {x2}")
        print(f"f(x2) atual: {fx2}")
        historico.append({"iteracao" : i, "x" : x2, "fx" : fx2})
        if abs(fx2) < tolerancia:
            break
        else:
            x0 = x1
            x1 = x2
        print("================================================")
     return historico
