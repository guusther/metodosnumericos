from pathlib import Path
import sys

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROJETO))

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from InterpolacaoPolinomial.definicao import (
    montar_matriz_vandermonde,
    montar_termos,
    validar_pontos as validar_definicao,
    formatar_polinomio as formatar_definicao,
)
from InterpolacaoPolinomial.polinomio_newton import (
    calcular_polinomio as calcular_newton,
    diferencas_divididas,
    formatar_polinomio as formatar_newton,
    validar_pontos as validar_newton,
)
from SistemasLineares.eliminacao_gauss import (
    montar_matriz_aumentada,
    resolver_sistema,
)
from AjusteCurvas.ajuste_polinomial import calcular_polinomio as calcular_definicao


st.set_page_config(page_title="Interpolação Polinomial", page_icon="📈", layout="wide")
st.title("Interpolação Polinomial")
st.caption("Compare os dois métodos e visualize o polinômio passando pelos pontos informados.")

with st.sidebar:
    st.header("Configurações")
    metodo = st.selectbox(
        "Método de interpolação",
        ["Definição (Vandermonde)", "Newton (diferenças divididas)"],
    )
    valor_x = st.number_input("Calcular P(x) em:", value=2.5, format="%.6f")
    mostrar_tabela = st.checkbox("Mostrar tabela de diferenças divididas", value=True)

st.subheader("Pontos conhecidos")
st.write("Edite a tabela abaixo. Cada linha representa um ponto (x, y).")
dados_iniciais = pd.DataFrame({"x": [1.0, 2.0, 3.0], "y": [2.0, 3.0, 5.0]})
dados = st.data_editor(
    dados_iniciais,
    num_rows="dynamic",
    use_container_width=True,
    key="tabela_pontos_interpolacao",
    column_config={
        "x": st.column_config.NumberColumn("x", required=True, format="%.6f"),
        "y": st.column_config.NumberColumn("f(x)", required=True, format="%.6f"),
    },
)

if st.button("Interpolar", type="primary"):
    try:
        if dados.empty or dados[["x", "y"]].isnull().any().any():
            raise ValueError("Preencha x e y em todas as linhas.")

        pontos = [
            (float(linha.x), float(linha.y))
            for linha in dados.itertuples(index=False)
        ]

        xs = [p[0] for p in pontos]

        if len(pontos) < 2:
            raise ValueError("Informe pelo menos dois pontos.")

        if len(xs) != len(set(xs)):
            raise ValueError("Os valores de x precisam ser distintos.")

        if metodo == "Definição (Vandermonde)":
            validar_definicao(pontos)
            matriz = montar_matriz_vandermonde(pontos)
            termos = montar_termos(pontos)
            matriz_aumentada = montar_matriz_aumentada(matriz, termos)
            coeficientes = resolver_sistema(matriz_aumentada)

            polinomio = formatar_definicao(coeficientes)
            avaliar = lambda v: calcular_definicao(coeficientes, v)
            detalhe = "Coeficientes em ordem crescente: a₀, a₁, a₂, ..."

        else:
            validar_newton(pontos)
            polinomio = formatar_newton(pontos)
            avaliar = lambda v: calcular_newton(pontos, v)
            detalhe = "Forma de Newton construída com diferenças divididas."

        resultado = avaliar(float(valor_x))

        st.success("Polinômio interpolador calculado.")
        st.markdown("**Polinômio encontrado**")
        st.code(f"P(x) = {polinomio}")

        c1, c2 = st.columns(2)
        c1.metric(f"P({valor_x:g})", f"{resultado:.8f}")
        c2.metric("Pontos utilizados", len(pontos))

        st.caption(detalhe)

        # Domínio com margem para tornar a curva legível.
        x_min, x_max = min(xs), max(xs)
        margem = (x_max - x_min) * 0.12 or 1.0
        dominio = np.linspace(x_min - margem, x_max + margem, 500)
        curva = [avaliar(float(v)) for v in dominio]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=dominio,
            y=curva,
            mode="lines",
            name="Polinômio interpolador",
            line=dict(width=3)
        ))

        fig.add_trace(go.Scatter(
            x=xs,
            y=[p[1] for p in pontos],
            mode="markers+text",
            text=[f"({x:g}, {y:g})" for x, y in pontos],
            textposition="top center",
            name="Pontos informados",
            marker=dict(size=11, symbol="circle")
        ))

        fig.add_vline(x=float(valor_x), line_dash="dot", opacity=0.55)

        fig.add_trace(go.Scatter(
            x=[float(valor_x)],
            y=[resultado],
            mode="markers",
            name=f"P({valor_x:g})",
            marker=dict(size=10, symbol="x")
        ))

        fig.update_layout(
            title="Visualização do polinômio interpolador",
            xaxis_title="x",
            yaxis_title="P(x)",
            height=570,
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "Verificação: a curva deve passar por todos os pontos conhecidos. "
            "Isso é interpolação; não é uma aproximação por mínimos quadrados."
        )

        if metodo == "Newton (diferenças divididas)" and mostrar_tabela:
            st.subheader("Tabela de diferenças divididas")

            tabela = diferencas_divididas(pontos)
            colunas = ["f[x]"] + [
                f"Ordem {i}" for i in range(1, len(pontos))
            ]

            linhas = []

            for i, ponto in enumerate(pontos):
                linha = {"x": ponto[0]}

                for j, nome in enumerate(colunas):
                    linha[nome] = (
                        tabela[i][j]
                        if i + j < len(pontos)
                        else None
                    )

                linhas.append(linha)

            st.dataframe(
                pd.DataFrame(linhas),
                use_container_width=True
            )

    except Exception as erro:
        st.error(f"Não foi possível calcular a interpolação: {erro}")
