from AjusteCurvas.ajuste_polinomial import (
    calcular_polinomio,
    pedir_ponto
)
from SistemasLineares.eliminacao_gauss import (
    montar_matriz_aumentada,
    resolver_sistema
)

def montar_matriz_vandermonde(pontos):
    matriz = []
    
    for x, y in pontos:
        linha = []
        for j in range(len(pontos)):
            linha.append(x ** j)
        matriz.append(linha)
    
    return matriz

def montar_termos(pontos):
    lista_termos = []
    for x, y in pontos:
        lista_termos.append(y)
    return lista_termos

def validar_pontos(pontos):
    if len(pontos) < 2:
        raise ValueError("São necessários pelo menos dois pontos")
    
    valores_x = [x for x,y in pontos]
    
    if len(valores_x) != len(set(valores_x)):
        raise ValueError("Os valores de x devem ser distintos")


if __name__ == "__main__":
    pontos = pedir_ponto()
    validar_pontos(pontos)

    matriz = montar_matriz_vandermonde(pontos)
    b = montar_termos(pontos)

    matriz = montar_matriz_aumentada(matriz, b)
    solucao = resolver_sistema(matriz)
    resultado = calcular_polinomio(solucao, 4)

    print(solucao)
    print(resultado)