from SistemasLineares.eliminacao_gauss import montar_matriz_aumentada, resolver_sistema

def pedir_ponto():
    pontos = []
    qtd_pontos = int(input("Digite quantos pontos o sistema terá:"))
    
    for i in range(qtd_pontos):
        coordenadas = []
        x = float(input(f"Digite a coordenada x do {i + 1}o ponto :"))
        coordenadas.append(x)
        
        y = float(input(f"Digite a coordenada y do {i + 1}o ponto :"))
        coordenadas.append(y)
        
        pontos.append(coordenadas)
        
    return pontos

def pedir_grau():
    grau = int(input("Digite o grau desejado do polinômio: "))
    return grau

def montar_matriz_normal(grau, pontos):
    tamanho = grau + 1
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            soma = 0
            for x, y in pontos:
                soma += x ** (i + j)
            
            linha.append(soma)
        matriz.append(linha)
    return matriz
            
def montar_termo(grau, pontos):
    tamanho = grau + 1
    termos = []
    for i in range(tamanho):
        soma = 0
        for x, y in pontos:
            soma += (y * (x ** i))
        termos.append(soma)
    return termos
        
def matriz_aumentada(matriz, termos):
    return montar_matriz_aumentada(matriz, termos)    

def calcular_polinomio(coeficientes, x):
    resultado = 0
    
    for i in range(len(coeficientes)):
        resultado += coeficientes[i] * (x ** i)
    return resultado
    
def validar_dados(grau, pontos):
    qtd_pontos = len(pontos)
    if qtd_pontos < grau + 1:
        raise ValueError("quantidade insuficiente de pontos.")
    
    valores_x = [x for x, y in pontos]
    qtd_x_distintos = len(set(valores_x))
    
    if qtd_x_distintos < grau + 1:
        raise ValueError("quantidade insuficiente de valores de x distintos.")

if __name__ == "__main__":
    pontos = pedir_ponto()
    grau = pedir_grau()
    
    validar_dados(grau, pontos)
    
    matriz = montar_matriz_normal(grau, pontos)
    termos = montar_termo(grau, pontos)
    
    matriz = montar_matriz_aumentada(matriz, termos)
    
    coeficientes = resolver_sistema(matriz)
    resultado = calcular_polinomio(coeficientes, 1)
    
    print("Coeficientes:", coeficientes)
    print("Resultado: ", resultado)