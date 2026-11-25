def receber_sistema():
    num_incognitas = int(input("Digite quantas incógnitas o sistema terá: "))
    termmos_independentes = int(input("Digite quantos termos independentes o sistema terá:"))
    matriz = []
    for i in range(termmos_independentes):
        linha = []
        for j in range(num_incognitas):
           coeficiente = float(input(f"Digite o coeficiente da {j + 1}o incógnita da {i + 1}a linha:"))
           linha.append(coeficiente)
        matriz.append(linha)

    b = []
    for i in range(termmos_independentes):
        numero = float(input(f"Digite o {i + 1}o termo indepedente:"))
        b.append(numero)

    return matriz, b

def montar_matriz_aumentada(A,b):
    matriz_aumentada = []
    for i in range(len(A)):
        A[i].append(b[i])
        matriz_aumentada.append(A[i])
    return matriz_aumentada

def encontrar_linha_pivo(matriz, p):
    linha_pivo = p

    for i in range(p + 1, len(matriz)):
        if abs(matriz[i][p]) > abs(matriz[linha_pivo][p]):
            linha_pivo = i
    return linha_pivo

def eliminacao_gauss(matriz):
    for p in range(len(matriz) - 1):

        linha_pivo = encontrar_linha_pivo(matriz, p)

        if abs(matriz[linha_pivo][p]) < 1e-12:
            raise ValueError("Sistema sem solucao unica.")
        matriz[p], matriz[linha_pivo] = matriz[linha_pivo], matriz[p]
        

        pivo = matriz[p][p]

        for i in range(p + 1, len(matriz)):
            multiplicador = matriz[i][p] / pivo
            for j in range(len(matriz[i])):
                matriz[i][j] = matriz[i][j] - (multiplicador * matriz[p][j])

    return matriz

def substituicao_retroativa(matriz):
    n = len(matriz)
    solucoes = [0] * n

    for i in range(n - 1, -1, -1):
        soma = 0

        for j in range(i + 1, n):
            soma += matriz[i][j] * solucoes[j]

        solucoes[i] = (matriz[i][-1] - soma) / matriz[i][i]

    return solucoes

def resolver_sistema(matriz):
    matriz = eliminacao_gauss(matriz)
    solucoes = substituicao_retroativa(matriz)

    solucoes = [round(valor, 10) for valor in solucoes]
    return solucoes

if __name__ == "__main__":
    a, b = receber_sistema()
    matriz = montar_matriz_aumentada(a, b)

    resultado = resolver_sistema(matriz)
    print("Soluções:", resultado)

