from eliminacao_gauss import encontrar_linha_pivo, receber_sistema

def aplicar_permutacao(P, b):
    n = len(P)
    novo_b = [0] * n
    
    for i in range(n):
        for j in range(n):
            novo_b[i] += P[i][j] * b[j]
    return novo_b

def substituicao_progressiva(L, b):
    n = len(L)
    y = [0] * n
    
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i][j] * y[j]
        y[i] = (b[i] - soma) / L[i][i]
    return y

def substituicao_regressiva(U, y):
    n = len(U)
    x = [0] *n
    
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += U[i][j] * x[j]
        x[i] = (y[i] - soma) / U[i][i]
    return x

def fatoracao_lu(matriz):
    
    n = len(matriz)

    U = [linha[:] for linha in matriz]

    L = [[0] * n for _ in range(n)]
    P = [[0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1
        P[i][i] = 1

    for p in range(n - 1):
        linha_pivo = encontrar_linha_pivo(U, p)
        
        U[p], U[linha_pivo] = U[linha_pivo], U[p]
        P[p], P[linha_pivo] = P[linha_pivo], P[p]
        
        for j in range(p):
            L[p][j], L[linha_pivo][j] = L[linha_pivo][j], L[p][j]

        pivo = U[p][p]
        
        if abs(pivo) < 1e-12:
            raise ValueError("Matriz singular ou sem pivô adequado.")
        
        for i in range(p + 1, len(U)):
            multiplicador = U[i][p] / pivo
            L[i][p] = multiplicador
            for k in range(p, n):
                U[i][k] = U[i][k] - (multiplicador * U[p][k])
    if abs(U[n - 1][n - 1]) < 1e-12:
        raise ValueError("Matriz singular ou sem solução única.")
        
    return L, U, P

def resolver_sistema_lu(A,b):
    L,U,P = fatoracao_lu(A)
    novo_b = aplicar_permutacao(P, b)
    y = substituicao_progressiva(L, novo_b)
    x = substituicao_regressiva(U, y)
    
    return x

def exibir_matriz(nome, matriz):
    print(f"\n{nome}:")
    for linha in matriz:
        print("[", "  ".join(f"{valor:8.2f}" for valor in linha), "]")

def exibir_solucoes(x):
    print("\nSoluções:")
    for i, valor in enumerate(x):
        print(f"x{i + 1} = {valor:.2f}")

if __name__ == "__main__":
    matriz, b = receber_sistema()
    L, U, P = fatoracao_lu(matriz)

    x = resolver_sistema_lu(matriz, b)

    print("\n========== FATORAÇÃO LU ==========")
    exibir_matriz("Matriz L", L)
    exibir_matriz("Matriz U", U)
    exibir_matriz("Matriz P", P)
    exibir_solucoes(x)