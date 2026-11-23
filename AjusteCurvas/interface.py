import sys
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROJETO))

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from AjusteCurvas.ajuste_polinomial import (
    calcular_polinomio,
    montar_matriz_normal,
    montar_termo,
    validar_dados,
)
from SistemasLineares.eliminacao_gauss import (
    montar_matriz_aumentada,
    resolver_sistema,
)

st.set_page_config(page_title="Ajuste de Curvas", layout="wide")
st.title("Método dos Mínimos Quadrados")

st.write(
    "Informe os pontos, escolha o grau do polinômio e calcule o ajuste."
)

with st.sidebar:
    st.header("Parâmetros")

    quantidade = st.number_input(
        "Quantidade de pontos",
        min_value=1,
        max_value=100,
        value=5,
        step=1,
    )

    grau = st.number_input(
        "Grau do polinômio",
        min_value=0,
        max_value=10,
        value=1,
        step=1,
    )

    st.divider()
    st.subheader("Avaliar o polinômio")

    valor_x = st.number_input(
        "Valor de x",
        value=1.0,
        format="%.6f",
    )

st.subheader("Pontos")
st.caption("Preencha as coordenadas x e y de cada ponto.")

with st.form("form_ajuste"):
    colunas = st.columns(2)
    colunas[0].markdown("**Coordenada x**")
    colunas[1].markdown("**Coordenada y**")

    pontos = []

    for i in range(int(quantidade)):
        col_x, col_y = st.columns(2)

        with col_x:
            x = st.number_input(
                f"x do ponto {i + 1}",
                value=float(i),
                key=f"x_{i}",
                format="%.6f",
            )

        with col_y:
            y = st.number_input(
                f"y do ponto {i + 1}",
                value=0.0,
                key=f"y_{i}",
                format="%.6f",
            )

        pontos.append([x, y])

    calcular = st.form_submit_button(
        "Calcular ajuste",
        type="primary",
        use_container_width=True,
    )

if calcular:
    try:
        validar_dados(int(grau), pontos)

        matriz = montar_matriz_normal(int(grau), pontos)
        termos = montar_termo(int(grau), pontos)

        matriz = montar_matriz_aumentada(matriz, termos)
        coeficientes = resolver_sistema(matriz)

        valores_y_ajustados = [
            calcular_polinomio(coeficientes, x)
            for x, y in pontos
        ]

        erro_total = sum(
            (y - y_ajustado) ** 2
            for (_, y), y_ajustado in zip(pontos, valores_y_ajustados)
        )

        resultado_x = calcular_polinomio(coeficientes, valor_x)

        st.success("Ajuste calculado com sucesso!")

        st.subheader("Polinômio encontrado")

        termos_equacao = []

        for i, coeficiente in enumerate(coeficientes):
            if i == 0:
                termos_equacao.append(f"{coeficiente:.6g}")
            elif i == 1:
                termos_equacao.append(f"{coeficiente:.6g}x")
            else:
                termos_equacao.append(f"{coeficiente:.6g}x^{i}")

        st.latex(
            "P(x) = " +
            " + ".join(termos_equacao).replace("+ -", "- ")
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Erro total quadrático",
                f"{erro_total:.8f}",
            )

        with col2:
            st.metric(
                f"P({valor_x:g})",
                f"{resultado_x:.8f}",
            )

        st.subheader("Coeficientes")

        tabela_coeficientes = {
            "Coeficiente": [
                f"a{i}" for i in range(len(coeficientes))
            ],
            "Valor": coeficientes,
        }

        st.dataframe(
            tabela_coeficientes,
            hide_index=True,
            use_container_width=True,
        )

        st.subheader("Gráfico do ajuste")

        valores_x = [ponto[0] for ponto in pontos]

        minimo_x = min(valores_x)
        maximo_x = max(valores_x)

        if minimo_x == maximo_x:
            minimo_x -= 1
            maximo_x += 1

        dominio = np.linspace(minimo_x, maximo_x, 300)

        curva = [
            calcular_polinomio(coeficientes, x)
            for x in dominio
        ]

        figura = go.Figure()

        figura.add_trace(
            go.Scatter(
                x=valores_x,
                y=[ponto[1] for ponto in pontos],
                mode="markers",
                name="Pontos informados",
                marker=dict(size=10),
            )
        )

        figura.add_trace(
            go.Scatter(
                x=dominio,
                y=curva,
                mode="lines",
                name="Polinômio ajustado",
            )
        )

        figura.update_layout(
            xaxis_title="x",
            yaxis_title="y",
            height=550,
            hovermode="x unified",
        )

        st.plotly_chart(
            figura,
            use_container_width=True,
        )

    except (ValueError, ZeroDivisionError) as erro:
        st.error(f"Não foi possível calcular o ajuste: {erro}")

    except Exception as erro:
        st.error(f"Ocorreu um erro inesperado: {erro}")
