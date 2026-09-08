from sympy import symbols
from sympy import diff
from sympy import lambdify

def bissecao(limA, limB, funcao, tolerancia):
    if funcao(limA) * funcao(limB) > 0:
        raise ValueError(f"Não há garantia de raiz no intervalo [{limA}, {limB}]: f(limA) e f(limB) têm o mesmo sinal")
    historico = []

    while limB - limA > tolerancia:
        i = len(historico) + 1
        
        medio = (limA + limB)/2
        fx = funcao(medio)
        if (funcao(limA) < 0 and fx > 0) or (funcao(limA) > 0 and fx < 0):
            limB = medio
        else:
            limA = medio
        historico.append({"iteracao": i, "x" : medio, "fx" : fx})

    return historico



