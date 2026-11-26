
from sympy import symbols, sympify, lambdify
from sympy.core.sympify import SympifyError

x = symbols('x')


def pedir_funcao():
    texto_usuario = input(
        "Digita a função: (ex: x**3 - x - 2): "
    )

    try:
        expressao = sympify(texto_usuario)
        funcao = lambdify(x, expressao)
        return expressao, funcao

    except (SympifyError, SyntaxError, TypeError):
        raise ValueError(
            "A expressão matemática digitada é inválida."
        )


def calculo_h(limA, limB, subintervalos):
    return (limB - limA) / subintervalos


def pedir_subintervalos():
    subintervalos = int(
        input("Digite a quantidade de subintervalos: ")
    )
    return subintervalos


def validar_subintervalos(subintervalos):
    if subintervalos <= 0 or subintervalos % 2 != 0:
        raise ValueError(
            "A quantidade de subintervalos deve ser positiva e par."
        )


def calculo_intermediarios(limA, h, subintervalos, funcao):
    soma = 0

    for i in range(1, subintervalos):
        x = limA + i * h

        if i % 2 == 0:
            soma += 2 * funcao(x)

        else:
            soma += 4 * funcao(x)

    return soma


def simpson_repetido(limA, limB, funcao):
    subintervalos = pedir_subintervalos()

    validar_subintervalos(subintervalos)

    h = calculo_h(limA, limB, subintervalos)

    intermediarios = calculo_intermediarios(
        limA,
        h,
        subintervalos,
        funcao
    )

    fx0 = funcao(limA)
    fxn = funcao(limB)

    I = (h / 3) * (
        fx0 + intermediarios + fxn
    )

    return I


def pedir_limite(mensagem):
    while True:
        try:
            limite = float(input(mensagem))
            return limite

        except ValueError:
            print("Digite um valor numérico válido.")


def pedir_limites():
    limA = pedir_limite(
        "Digite o valor do limite inferior: "
    )

    limB = pedir_limite(
        "Digite o valor do limite superior: "
    )

    return limA, limB


if __name__ == "__main__":

    print("\n========== MÉTODO DE SIMPSON REPETIDO ==========")

    limA, limB = pedir_limites()

    expressao, funcao = pedir_funcao()

    resultado = simpson_repetido(
        limA,
        limB,
        funcao
    )

    print("\n========== RESULTADO ==========")
    print(f"Integral aproximada: {resultado:.6f}")
