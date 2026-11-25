
from AjusteCurvas.ajuste_polinomial import pedir_ponto


def validar_pontos(pontos):
    if len(pontos) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    valores_x = [x for x, y in pontos]

    if len(valores_x) != len(set(valores_x)):
        raise ValueError("Os valores de x devem ser distintos.")


def calcular_polinomio(pontos, valor):
    resultado = 0

    for i in range(len(pontos)):
        xi, yi = pontos[i]
        produto = 1

        for j in range(len(pontos)):
            if i != j:
                xj = pontos[j][0]

                produto *= (valor - xj) / (xi - xj)

        resultado += yi * produto

    return resultado


def formatar_polinomio(pontos):
    termos = []

    for i in range(len(pontos)):
        xi, yi = pontos[i]

        numerador = []
        denominador = 1

        for j in range(len(pontos)):
            if i != j:
                xj = pontos[j][0]

                numerador.append(f"(x - {xj:g})")
                denominador *= xi - xj

        if numerador:
            produto = " * ".join(numerador)
            termo = f"{yi:g} * ({produto}) / ({denominador:g})"
        else:
            termo = f"{yi:g}"

        termos.append(termo)

    return " + ".join(termos)


if __name__ == "__main__":
    print("\n========== INTERPOLAÇÃO POLINOMIAL DE LAGRANGE ==========")

    pontos = pedir_ponto()
    validar_pontos(pontos)

    polinomio = formatar_polinomio(pontos)

    valor = float(input("\nDigite o valor que deseja interpolar: "))

    resultado = calcular_polinomio(pontos, valor)

    print(f"\nPolinômio interpolador: P(x) = {polinomio}")
    print(f"\nP({valor}) = {resultado:.6f}")
