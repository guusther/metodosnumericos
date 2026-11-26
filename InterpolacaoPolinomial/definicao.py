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

def formatar_polinomio(coeficientes):
    termos = []

    for grau, coeficiente in enumerate(coeficientes):

        if abs(coeficiente) < 1e-12:
            continue

        valor = f"{abs(coeficiente):.4f}".rstrip("0").rstrip(".")

        if grau == 0:
            termo = valor

        else:
            variavel = "x" if grau == 1 else f"x^{grau}"

            if abs(abs(coeficiente) - 1) < 1e-12:
                termo = variavel
            else:
                termo = f"{valor}{variavel}"

        if not termos:
            if coeficiente < 0:
                termo = "-" + termo

        else:
            sinal = " - " if coeficiente < 0 else " + "
            termo = sinal + termo

        termos.append(termo)

    return "".join(termos) if termos else "0"


if __name__ == "__main__":
    print("\n========== INTERPOLAÇÃO POLINOMIAL POR DEFINIÇÃO ==========")

    pontos = pedir_ponto()
    validar_pontos(pontos)

    matriz = montar_matriz_vandermonde(pontos)
    b = montar_termos(pontos)

    matriz = montar_matriz_aumentada(matriz, b)
    solucao = resolver_sistema(matriz)

    polinomio = formatar_polinomio(solucao)

    valor_x = float(
        input("\nDigite o valor que deseja interpolar: ")
    )

    resultado = calcular_polinomio(solucao, valor_x)

    print("\n========== RESULTADO ==========")
    print(f"Polinômio interpolador: P(x) = {polinomio}")
    print(f"\nValor interpolado:")
    print(f"P({valor_x}) = {resultado:.6f}")

    print("\n==============================================")
