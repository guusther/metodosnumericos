from funcoes.bissecao import bissecao
from funcoes.falsaposicao import falsa_posicao
from funcoes.secante import secante
from funcoes.newton import newton

from tabulate import tabulate

import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

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

def exibir_grid(limA, limB, funcao, resultados):
    nomes_metodos = [metodo for historico, metodo in resultados]
    fig = make_subplots(rows=2, cols=2, subplot_titles=nomes_metodos)

    x_dominio = np.linspace(limA, limB, 200)
    y_dominio = [funcao(x) for x in x_dominio]

    coordenadas = [(1,1), (1,2), (2,1), (2,2)]

    for(historico, metodo), (linha, coluna) in zip(resultados, coordenadas):
        fig.add_trace(go.Scatter(
            x = x_dominio, y=y_dominio, mode="lines", line=dict(color="blue"), name="f(x)",
            showlegend=(linha == 1 and coluna == 1)
        ), row=linha, col=coluna)

        x_hist = [p["x"] for p in historico]
        y_hist = [p["fx"] for p in historico]
        rotulos = [f"i={p.get('iteracao', p.get('iteração'))}" for p in historico]

        fig.add_trace(
            go.Scatter(
                x=x_hist, y=y_hist, mode="markers+text",
                text=rotulos, textposition="top center", name=metodo
            ),
            row=linha, col=coluna
        )

        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity = 0.5, row=linha, col=coluna)

    fig.update_layout(title="Comparação dos métodos(grid 2x2)", height=800)
    fig.write_html("relatorio_grid.html",auto_open=True)

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
    elif escolha == "5":
        x0 = pedir_chute()
        limA, limB = pedir_intervalo()

    #lambda serve para criar uma funcao anonima que serve como um botao de pausa, fazendo ela
    #nao ser executada na hora
    algoritmo = {
         "1": lambda: [(bissecao(limA, limB, funcao_matematica, tolerancia), "Bisseção")],
         "2": lambda: [(falsa_posicao(limA, limB, funcao_matematica, tolerancia), "Falsa Posição")],
         "3": lambda: [(secante(limA, limB, funcao_matematica, tolerancia), "Secante")],
         "4": lambda: [(newton(x0, expressao, funcao_matematica, tolerancia), "Newton")],
         "5": lambda: [(bissecao(limA, limB, funcao_matematica, tolerancia), "Bisseção"), 
                       (falsa_posicao(limA, limB, funcao_matematica, tolerancia), "Falsa Posição"),
                       (secante(limA, limB, funcao_matematica, tolerancia), "Secante"),
                       (newton(x0, expressao, funcao_matematica, tolerancia), "Newton")]
    }
    resultados = algoritmo[escolha]()
    for historico, metodo in resultados:
        print(f"--{metodo}--")
        print(tabulate(historico, headers="keys", tablefmt="grid", floatfmt=".6f"))

    if escolha == "5":
        exibir_grid(limA, limB, funcao_matematica, resultados)
    else:
        historico_unico, metodo_unico = resultados[0]
        exibir_relatorio(limA, limB, funcao_matematica, historico_unico, metodo_unico)


executar()
        