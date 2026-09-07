from sympy import symbols
from sympy import diff
from sympy import lambdify

def bissecao(limA, limB, funcao, tolerancia):
    historico = []

    print(f"intervalo inicial: [{limA}, {limB}]")
    i = 1
    while limB - limA > tolerancia:
        print(f"Iteração {i + 1}:")
        i = i + 1
        medio = (limA + limB)/2
        fx = funcao(medio)
        if (funcao(limA) < 0 and fx > 0) or (funcao(limA) > 0 and fx < 0):
            limB = medio
        else:
            limA = medio
        historico.append({"iteracao": i, "x_medio" : medio, "fx" : fx})
        print(f"Os limites no momento são: [{limA}, {limB}]")
        print("=====================================")

    return historico

print(bissecao(1, 2, funcao, 0.01))



