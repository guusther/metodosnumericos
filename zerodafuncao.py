
def funcao(x):
    return x**3 - x - 2

def bissecao(limA, limB, funcao, tolerancia):
    print("\\\\BISSEÇÃO////")
    print(f"intervalo inicial: [{limA}, {limB}]")
    i = 0
    while limB - limA > tolerancia:
        print(f"Iteração {i + 1}:")
        i = i + 1
        medio = (limA + limB)/2
        medio2 = funcao(medio)
        print(f"ponto medio: {medio}")
        print(f"f(medio): {medio2}")
        
        if (funcao(limA) < 0 and medio2 > 0) or (funcao(limA) > 0 and medio2 < 0):
            limB = medio
        else:
            limA = medio
        print(f"Os limites no momento são: [{limA}, {limB}]")
        print("=====================================")



def falsa_posicao(limA, limB, funcao, tolerancia):
    print("\\FALSA POSIÇÃO////")
    print(f"intervalo inicial: [{limA}, {limB}]")
    i = 0
    while limB - limA > tolerancia:
        print(f"Iteração {i + 1}:")
        i = i + 1
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
        print(f"Os limites no momento são: [{limA}, {limB}]")
        print("==============================================")
        if abs(fx) < tolerancia:
            break
        
def secante(x0, x1,funcao, tolerancia):
     i = 0
     while True:
        print(f"Iteração {i + 1}:")
        i = i + 1
        print(f"x0 e x1 atuais: {x0} e {x1}")
        fx1 = funcao(x1)
        fx0 = funcao(x0)
        x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        fx2 = funcao(x2)
        print(f"x2 atual: {x2}")
        print(f"f(x2) atual: {fx2}")
        if abs(fx2) < tolerancia:
            break
        else:
            x0 = x1
            x1 = x2
        print("================================================")



bissecao(1, 2, funcao, 0.01)                                    
print("||||||||||||||||||||||||||||||||||||||||")
falsa_posicao(1, 2, funcao, 0.01)
print("||||||||||||||||||||||||||||||||||||||||")
secante(1, 2, funcao, 0.01)