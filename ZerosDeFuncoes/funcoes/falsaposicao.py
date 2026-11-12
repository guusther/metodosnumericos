def falsa_posicao(limA, limB, funcao, tolerancia):
    if funcao(limA) * funcao(limB) > 0:
            raise ValueError(f"Não há garantia de raiz no intervalo [{limA}, {limB}]: f(limA) e f(limB) têm o mesmo sinal")
    historico = []
    
    
    while True:
        i = len(historico) + 1

        fA = funcao(limA)
        fB = funcao(limB)
        x = ((limA * fB) - (limB * fA)) / (fB - fA)
        fx = funcao(x)
        
        if fA * fx < 0:
            limB = x
        else:
            limA = x
        historico.append({"iteração" : i, "x" : x, "fx" : fx})
        
        if abs(fx) < tolerancia:
            break
    return historico
        