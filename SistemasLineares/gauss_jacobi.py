from eliminacao_gauss import receber_sistema
import math

def descobrir_incognitas(matriz):
    return len(matriz[0])

def criar_lista(incognitas):
    aproximacoes = [0] * incognitas
    return aproximacoes

def calcular_erro(aproximacoes_anteriores, novas_aproximacoes):
    erro = 0
    for i in range(len(aproximacoes_anteriores)):
        diferenca = abs(novas_aproximacoes[i] - aproximacoes_anteriores[i])
        
        if diferenca > erro:
            erro = diferenca
    return erro

def calcular_novas_aproximacoes(matriz, b, aproximacoes_anteriores):
    num_incognitas = descobrir_incognitas(matriz)
    
    max_iteracoes = 1000
    iteracao = 0
    
    tolerancia = 0.0001
    erro = float("inf")

    while erro > tolerancia and iteracao < max_iteracoes:
        
        iteracao+= 1
        
        novas_aproximacoes = criar_lista(num_incognitas)
        for i in range(num_incognitas):
            if matriz[i][i] == 0:
                raise ValueError("Não é possível aplicar Jacobi: existe um zero na diagonal principal")
            
            soma = 0
            for j in range(num_incognitas):
                if i != j:
                    soma += matriz[i][j] * aproximacoes_anteriores[j]
                    
                                        
            novas_aproximacoes[i] = (b[i] - soma)/ matriz[i][i] 
        
        if any(math.isnan(v) or math.isinf(v) for v in novas_aproximacoes):
            raise ValueError("O método divergiu (valores infinitos ou NaN).")    
        
        erro = calcular_erro(aproximacoes_anteriores, novas_aproximacoes)
        aproximacoes_anteriores = novas_aproximacoes       
    
    if erro > tolerancia:
        raise ValueError("O método não convergiu dentro do limite de iterações.")
    
    return aproximacoes_anteriores 
        

if __name__ == "__main__":
    print("\n========== MÉTODO DE GAUSS-JACOBI ==========")

    matriz, b = receber_sistema()

    num_incognitas = len(matriz[0])
    aproximacoes_iniciais = criar_lista(num_incognitas)

    solucoes = calcular_novas_aproximacoes(
        matriz,
        b,
        aproximacoes_iniciais
    )

    print("\n========== RESULTADO ==========")
    print("Soluções do sistema:\n")

    for i, valor in enumerate(solucoes):
        print(f"x{i + 1} = {valor:.6f}")

    print("\n==============================================")
