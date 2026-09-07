from funcoes.bissecao import bissecao
from funcoes.falsaposicao import falsa_posicao
from funcoes.secante import secante
from funcoes.newton import newton

def funcao(x):
    return x**3 - x - 2

hist_bissecao = bissecao(1, 2, funcao, 0.01)
hist_falsa = falsa_posicao(1, 2, funcao, 0.01)
hist_secante= secante(1, 2, funcao, 0.01)
hist_newton = newton(2, funcao, 0.01)

print(hist_bissecao)
print("====================")
print(hist_falsa)
print("====================")
print(hist_secante)
print("====================")
print(hist_newton)