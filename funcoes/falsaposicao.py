from sympy import symbols
from sympy import diff
from sympy import lambdify

def funcao(x):
    return x**3 - x - 2

def falsa_posicao(limA, limB, funcao, tolerancia):
    historico = []
    print("\\FALSA POSIÇÃO////")
    print(f"intervalo inicial: [{limA}, {limB}]")
    i = 1
    while limB - limA > tolerancia:
        print(f"Iteração {i + 1}:")
        fA = funcao(limA)
        fB = funcao(limB)
        x = ((limA * fB) - (limB * fA)) / (fB - fA)
        fx = funcao(x)
        print(f"o x eh: {x}")
        print(f"o f(x) eh: {fx}")
        if fA * fx < 0:
            limB = x
        else:
            limA = x
        historico.append({"iteração" : i, "x" : x, "fx" : fx})
        print(f"Os limites no momento são: [{limA}, {limB}]")
        print("==============================================")
        if abs(fx) < tolerancia:
            break
    return historico
        