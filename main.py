from funcoes.bissecao import bissecao
from funcoes.falsaposicao import falsa_posicao
from funcoes.secante import secante
from funcoes.newton import newton

import plotly.graph_objects as go
import numpy as np

from sympy import symbols, sympify, lambdify

x = symbols('x')

def montar_grafico(x_vals, y_vals, metodos):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", name="f(x)"))

    for nome, historico in metodos.items():

        rotulos = [f"i={p.get('iteracao', p.get('iteração'))}" for p in historico]

        fig.add_trace(go.Scatter(x=[p["x"] for p in historico], y=[p["fx"] for p in historico], 
                                 mode="markers+text", text=rotulos, textposition="top center", name=nome))

        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5, annotation_text="Raiz (y = 0)")

    fig.update_layout(title="Convergência dos métodos de zero de função", xaxis_title="x", yaxis_title="f(x)")

    return fig

def funcao():
    texto_usuario = input("Digita a função: (ex: x**3 - x - 2)")
    expressao = sympify(texto_usuario)
    funcao = lambdify(x, expressao)
    return expressao, funcao

def menu():
    print("Qual método você quer visualizar?")
    print("1 - Bisseção")
    print("2 - Falsa Posição")
    print("3 - Secante")
    print("4 - Newton-Raphson")
    print("5 - Comparação geral")

    escolha = input("Digite o número da opção: ")
    return escolha

def pedir_intervalo():
    limA = float(input("Digite o valor do limite inferior/aproximação inicial qualquer: "))
    limB = float(input("Digite o valor do limite superior/aproximação inicial qualquer: "))
    return limA, limB

def pedir_chute():
    x0 = float(input("Digite o chute inicial: "))
    return x0

def exibir_relatorio(limA, limB, funcao, historico, metodo):
    x_vals = np.linspace(limA, limB, 200)
    y_vals = [funcao(x) for x in x_vals]

    fig = montar_grafico(x_vals, y_vals, {metodo: historico})
    fig.write_html("relatorio.html",auto_open=True)


def executar():
    escolha = menu()

    expressao, funcao_matematica = funcao()
    tolerancia = float(input("Digite a tolerância: "))

    if escolha in ("1", "2", "3"):
        
        limA, limB = pedir_intervalo()
        
    elif escolha == "4":
        x0 = pedir_chute()
        limA, limB = x0 - 2, x0 + 2

    #lambda serve para criar uma funcao anonima que serve como um botao de pausa, fazendo ela
    #nao ser executada na hora
    algoritmo = {
         "1": lambda: (bissecao(limA, limB, funcao_matematica, tolerancia), "Bisseção"),
         "2": lambda: (falsa_posicao(limA, limB, funcao_matematica, tolerancia), "Falsa Posição"),
         "3": lambda: (secante(limA, limB, funcao_matematica, tolerancia), "Secante"),
         "4": lambda: (newton(x0, expressao, funcao_matematica, tolerancia), "Newton")
    }
    historico, metodo = algoritmo[escolha]() #os () no final faz despausar a funcao

    exibir_relatorio(limA, limB, funcao_matematica, historico, metodo)


executar()
        
"""
linspace significa tipo: de 200 numeros entre 1 e 2 basicamente. Então se
no lugar do 200 fosse 5 seria algo do tipo [1.0, 1.25, 1.5, 1.75, 2]
Entretanto, ser 200 numeros faz com que a distancia seja bem menor q 0.25, portanto, quando o
grafico for desenhado, será uma linha continua ao inves de pontos separados

isso aqui eh a mesma coisa de um for com .append. Ele vai
calcular funcao(x) para cada um dos 200 e guardar numa lista

fig inicialmene eh uma tela em branco que ao decorrer vai sendo empilhada com 
camadas de desenho

o go.Scatter cria uma camada de desenho. Ela re
fig.add_trace(go.Scattcebe duas listas paralelas, sendo
nesse caso as listas dos valore de x e y. mode="lines" é pra ligar esses pontos 
com uma linha e o name é o texto que aparece na legenda do gráfico
"""