
from AjusteCurvas.ajuste_polinomial import pedir_ponto


def validar_pontos(pontos):
    if len(pontos) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    valores_x = [x for x, y in pontos]

    if len(valores_x) != len(set(valores_x)):
        raise ValueError("Os valores de x devem ser distintos.")


def diferencas_divididas(pontos):
    validar_pontos(pontos)

    quantidade = len(pontos)

    tabela = [[0.0] * quantidade for _ in range(quantidade)]

    for i in range(quantidade):
        tabela[i][0] = float(pontos[i][1])

    for ordem in range(1, quantidade):
        for i in range(quantidade - ordem):

            numerador = (
                tabela[i + 1][ordem - 1]
                - tabela[i][ordem - 1]
            )

            denominador = (
                pontos[i + ordem][0] - pontos[i][0]
            )

            tabela[i][ordem] = numerador / denominador

    return tabela


def coeficientes_newton(pontos):
    tabela = diferencas_divididas(pontos)

    return [
        tabela[0][i]
        for i in range(len(pontos))
    ]


def calcular_polinomio(pontos, valor):
    coeficientes = coeficientes_newton(pontos)

    resultado = coeficientes[-1]

    for i in range(len(coeficientes) - 2, -1, -1):
        resultado = (
            coeficientes[i]
            + (valor - pontos[i][0]) * resultado
        )

    return resultado


def mostrar_tabela(pontos):
    tabela = diferencas_divididas(pontos)
    quantidade = len(pontos)

    print("\nTabela de diferenças divididas:")

    cabecalho = ["x", "f[x]"] + [
        f"Ordem {i}"
        for i in range(1, quantidade)
    ]

    print(" | ".join(f"{item:>14}" for item in cabecalho))

    for i in range(quantidade):
        linha = [f"{pontos[i][0]:.6f}"]

        for ordem in range(quantidade):
            if i + ordem < quantidade:
                linha.append(f"{tabela[i][ordem]:.6f}")
            else:
                linha.append("")

        print(" | ".join(f"{item:>14}" for item in linha))


def formatar_polinomio(pontos):
    coeficientes = coeficientes_newton(pontos)

    termos = [f"{coeficientes[0]:.6g}"]

    for i in range(1, len(coeficientes)):
        fatores = " * ".join(
            f"(x - ({pontos[j][0]:.6g}))"
            for j in range(i)
        )

        termos.append(
            f"({coeficientes[i]:.6g}) * {fatores}"
        )

    return " + ".join(termos)


if __name__ == "__main__":

    print("\n========== INTERPOLAÇÃO POLINOMIAL DE NEWTON ==========")

    pontos = pedir_ponto()

    validar_pontos(pontos)

    mostrar_tabela(pontos)

    polinomio = formatar_polinomio(pontos)

    valor = float(
        input("\nDigite o valor que deseja interpolar: ")
    )

    resultado = calcular_polinomio(pontos, valor)

    print(f"\nPolinômio interpolador: P(x) = {polinomio}")

    print(f"\nP({valor}) = {resultado:.6f}")
