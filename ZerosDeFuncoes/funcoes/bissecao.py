def bissecao(limA, limB, funcao, tolerancia):
    fA = funcao(limA)
    fB = funcao(limB)
    if fA * fB > 0:
        raise ValueError(f"Não há garantia de raiz no intervalo [{limA}, {limB}]: f(limA) e f(limB) têm o mesmo sinal")
    historico = []

    while (limB - limA) > tolerancia:
        i = len(historico) + 1
        
        medio = (limA + limB)/2
        fx = funcao(medio)

        historico.append({"iteracao": i, "x":medio, "fx": fx})

        if abs(fx) < tolerancia:
            break

        if fA * fx < 0:
            limB = medio
        else:
            limA = medio
            fA = fx
    return historico



