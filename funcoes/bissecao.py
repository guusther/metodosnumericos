from sympy import symbols
from sympy import diff
from sympy import lambdify

def bissecao(limA, limB, funcao, tolerancia):
    historico = []

    print(f"intervalo inicial: [{limA}, {limB}]")
    
    while limB - limA > tolerancia:
        i = len(historico) + 1
        print(f"Iteração {i}:")
        
        medio = (limA + limB)/2
        fx = funcao(medio)
        if (funcao(limA) < 0 and fx > 0) or (funcao(limA) > 0 and fx < 0):
            limB = medio
        else:
            limA = medio
        historico.append({"iteracao": i, "x" : medio, "fx" : fx})
        print(f"Os limites no momento são: [{limA}, {limB}]")
        print("=====================================")

    return historico



