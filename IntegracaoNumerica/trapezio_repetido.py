from sympy import symbols, sympify, lambdify

x = symbols('x')

def pedir_funcao():
    texto_usuario = input("Digita a função: (ex: x**3 - x - 2)")
    expressao = sympify(texto_usuario)
    funcao = lambdify(x, expressao)
    return expressao, funcao

def calculo_h(limA, limB, subintervalos):
    return (limB - limA) / subintervalos

def pedir_subintervalos():
    subintervalos = int(input("Digite a quantidade de subintervalos: "))
    return subintervalos

def calculo_intermediarios(limA, h, subintervalos, funcao):
    soma = 0
    for i in range(1, subintervalos):
        x = limA + i * h
        soma += funcao( x)
    return 2 * soma
    
def trapezio_repetido(limA, limB, funcao):
    subintervalos = pedir_subintervalos()
    h = calculo_h(limA, limB, subintervalos)
    
    intermediarios = calculo_intermediarios(limA, h, subintervalos, funcao)

    fx0 = funcao(limA)
    fxn = funcao(limB)
    
    I = h/2 * (fx0 + intermediarios + fxn)
    
    return I

def pedir_limites():
    limA = float(input("Digite o valor do limite inferior:"))
    limB = float(input("Digite o valor do limite superior:"))
    return limA, limB

if __name__ == "__main__":
    limA, limB = pedir_limites()
    expressao, funcao = pedir_funcao()
    resultado = trapezio_repetido(limA, limB, funcao)
    print(resultado)