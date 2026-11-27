import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sympy import symbols, sympify, lambdify

#import das funcoes
from funcoes.bissecao import bissecao
from funcoes.falsaposicao import falsa_posicao
from funcoes.secante import secante
from funcoes.newton import newton

x = symbols('x')

#pag da larg do monitor
st.set_page_config(layout="wide")
st.title("Métodos de Zero de Função")

#funcao do grafico
def montar_grafico_st(x_vals, y_vals, metodos):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", name="f(x)"))

    for nome, historico in metodos.items():
        rotulos = [f"i={p.get('iteracao', p.get('iteração'))}" for p in historico]
        fig.add_trace(go.Scatter(x=[p["x"] for p in historico],
                                 y=[p["fx"] for p in historico],
                                 mode="markers+text", text=rotulos, textposition="top center", name=nome))
        fig.add_hline(y=0, line_dash="dash", line_color = "black", opacity=0.5, annotation_text="Raiz (y = 0)")

    fig.update_layout(title="Métodos de Zero de Função", xaxis_title="x",yaxis_title="y - f(x)", height=600)
    return fig

def exibir_grid_st(limA, limB, funcao, resultados):
    nomes_metodos = [metodo for historico, metodo in resultados]
    fig = make_subplots(rows=2, cols=2, subplot_titles=nomes_metodos)

    x_dominio = np.linspace(limA, limB, 200)
    y_dominio = [funcao(v) for v in x_dominio]

    coordenadas = [(1,1), (1,2), (2,1), (2,2)]

    for (historico, metodo), (linha, coluna) in zip(resultados, coordenadas):
        fig.add_trace(go.Scatter(x=x_dominio, y=y_dominio, mode="lines", line=dict(color="blue"), name="f(x)",
                                 showlegend=(linha == 1 and coluna == 1)), row=linha, col=coluna)

        x_hist = [p["x"] for p in historico]
        y_hist = [p["fx"] for p in historico]
        rotulos = [f"i={p.get('iteracao', p.get('iteração'))}" for p in historico]

        fig.add_trace(go.Scatter(x=x_hist, y=y_hist, mode="markers+text",
                                 text=rotulos, textposition="top center", name=metodo), row=linha, col=coluna)
        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5, row=linha, col=coluna)

    fig.update_layout(title="Comparação dos métodos (Grid 2x2)", height=700)
    return fig
#barra lateral
with st.sidebar:
    st.header("Paramêtros")

    opcoes = {
        "1": "Bisseção", "2": "Falsa Posição", "3": "Secante", "4": "Newton",
        "5": "Comparação Geral"
    }

    #selectbox cria uma caixa com seta pra baixo
    #o format_func faz mostrar o texto, mas o programa entende o número("1")
    escolha = st.selectbox("Qual método?", options=list(opcoes.keys()), format_func=lambda k: opcoes[k])

    texto_funcao = st.text_input("Digite a função f(x):", value="x**3 + x - 10")
    tolerancia = st.number_input("Tolerância:", value=0.0001, format="%.6f")

    limA, limB, x0 = 1.0, 3.0, 1.5

    #condicoes para so mostrar os limites se o metodo nao for o de newton
    if escolha in ("1", "2", "3", "5"):
        st.subheader("Intervalo")
        limA = st.number_input("Limite Inferior (A):", value=1.0)
        limB = st.number_input("Limite Inferior (B):", value=3.0)

    if escolha in ("4", "5"):
        st.subheader("Chute inicial")
        x0 = st.number_input("Chute inicial (x0):", value=1.5)

if st.button("Calcular Resultados", type="primary"):

    try:
        expressao = sympify(texto_funcao)
        funcao_matematica = lambdify(x, expressao)

        if escolha == "4":
            limA, limB = x0 - 2, x0 + 2

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

        aba_tabelas, aba_graficos = st.tabs(["Tabelas de Iteração", "Gráficos Visuais"]) 

        with aba_tabelas:
            for historico, metodo in resultados:
                st.subheader(f"Método: {metodo}")
                st.dataframe(historico, use_container_width=True)

        with aba_graficos:
            if escolha == "5":
                fig = exibir_grid_st(limA, limB, funcao_matematica, resultados)
                st.plotly_chart(fig, use_container_width=True)
            else:
                historico_unico, metodo_unico = resultados[0]
                x_vals = np.linspace(limA,limB, 200)
                y_vals = [funcao_matematica(v) for v in x_vals]
                fig = montar_grafico_st(x_vals, y_vals, {metodo_unico : historico_unico})
                st.plotly_chart(fig, use_container_width=True)
    except Exception as erro:
        st.error(f"Ocorreu um erro. Verifique os dados inseridos. Erro: {erro}")