import math
from eliminacao_gauss import receber_sistema


def descobrir_incognitas(matriz):
    return len(matriz[0])


def criar_lista(incognitas):
    aproximacoes = [0.0] * incognitas
    return aproximacoes


def calcular_erro(aproximacoes_anteriores, novas_aproximacoes):
    erro = 0

    for i in range(len(aproximacoes_anteriores)):
        diferenca = abs(
            novas_aproximacoes[i] - aproximacoes_anteriores[i]
        )

        if diferenca > erro:
            erro = diferenca

    return erro


def calcular_novas_aproximacoes(matriz, b, aproximacoes):
    num_incognitas = descobrir_incognitas(matriz)

    if len(matriz) != num_incognitas or len(b) != num_incognitas:
        raise ValueError("A matriz e o vetor b devem ter dimensões compatíveis.")

    max_iteracoes = 1000
    tolerancia = 0.0001
    erro = float("inf")
    iteracao = 0

    while erro > tolerancia and iteracao < max_iteracoes:
        iteracao += 1

        aproximacoes_anteriores = aproximacoes.copy()

        for i in range(num_incognitas):
            
            if any(math.isnan(v) or math.isinf(v) for v in aproximacoes):
                raise ValueError("O método divergiu (valores infinitos ou NaN).")
            
            if abs(matriz[i][i]) < 1e-12:
                raise ValueError(
                    "Não é possível aplicar Gauss-Seidel: "
                    "existe zero na diagonal principal."
                )

            soma = 0

            for j in range(num_incognitas):
                if i != j:
                    soma += matriz[i][j] * aproximacoes[j]

            aproximacoes[i] = (b[i] - soma) / matriz[i][i]

        erro = calcular_erro(
            aproximacoes_anteriores,
            aproximacoes
        )

    if erro > tolerancia:
        raise ValueError(
            "O método não convergiu dentro do limite de iterações."
        )

    return aproximacoes


if __name__ == "__main__":
    print("\n========== MÉTODO DE GAUSS-SEIDEL ==========")

    matriz, b = receber_sistema()

    num_incognitas = descobrir_incognitas(matriz)
    aproximacoes_iniciais = criar_lista(num_incognitas)

    solucoes = calcular_novas_aproximacoes(
        matriz,
        b,
        aproximacoes_iniciais
    )

    print("\nSoluções:")

    for i, valor in enumerate(solucoes):
        print(f"x{i + 1} = {valor:.6f}")
