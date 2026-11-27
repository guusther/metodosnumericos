from pathlib import Path
import sys

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROJETO))

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, sympify, lambdify
from sympy.core.sympify import SympifyError

from IntegracaoNumerica.trapezio_repetido import trapezio_repetido
from IntegracaoNumerica.simpson_1 import simpson_repetido

x = symbols("x")

st.set_page_config(page_title="Integração Numérica", page_icon="∫", layout="wide")
st.title("Integração Numérica")
st.caption("Veja como cada método divide a região e constrói a aproximação da integral.")

with st.sidebar:
    st.header("Parâmetros")
    metodo = st.selectbox("Método", ["Trapézios repetidos", "Simpson 1/3 repetido"])
    texto_funcao = st.text_input("Função f(x)", value="x**2")
    a = st.number_input("Limite inferior (a)", value=0.0, format="%.6f")
    b = st.number_input("Limite superior (b)", value=2.0, format="%.6f")
    n_min = 2 if metodo == "Simpson 1/3 repetido" else 1
    n = st.number_input(
        "Número de subintervalos",
        min_value=n_min,
        value=4 if metodo == "Simpson 1/3 repetido" else 4,
        step=2 if metodo == "Simpson 1/3 repetido" else 1,
    )
    if metodo == "Simpson 1/3 repetido":
        st.caption("A quantidade de subintervalos precisa ser par.")

if st.button("Calcular e visualizar", type="primary"):
    try:
        if a == b:
            raise ValueError("Os limites de integração não podem ser iguais.")
        if a > b:
            raise ValueError("O limite inferior precisa ser menor que o superior.")
        if metodo == "Simpson 1/3 repetido" and int(n) % 2 != 0:
            raise ValueError("Simpson 1/3 exige um número par de subintervalos.")

        try:
            expressao = sympify(texto_funcao)
            funcao = lambdify(x, expressao, modules=["numpy"])
        except (SympifyError, SyntaxError, TypeError) as erro:
            raise ValueError("A função informada não é uma expressão válida.") from erro

        n = int(n)
        h = (b - a) / n
        nos_x = np.linspace(a, b, n + 1)
        nos_y = np.asarray(funcao(nos_x), dtype=float)
        if nos_y.ndim == 0:
            nos_y = np.full_like(nos_x, float(nos_y))
        if not np.all(np.isfinite(nos_y)):
            raise ValueError("A função gerou valores indefinidos no intervalo escolhido.")

        if metodo == "Trapézios repetidos":
            resultado = trapezio_repetido(a, b, funcao, n)
        else:
            resultado = simpson_repetido(a, b, funcao, n)

        # Desenho da função e das regiões aproximadas.
        dominio = np.linspace(a, b, max(500, n * 80))
        valores = np.asarray(funcao(dominio), dtype=float)
        if valores.ndim == 0:
            valores = np.full_like(dominio, float(valores))

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dominio, y=valores, mode="lines", name="f(x)",
            line=dict(width=3)
        ))

        if metodo == "Trapézios repetidos":
            for i in range(n):
                fig.add_trace(go.Scatter(
                    x=[nos_x[i], nos_x[i], nos_x[i+1], nos_x[i+1]],
                    y=[0, nos_y[i], nos_y[i+1], 0],
                    mode="lines", fill="toself",
                    fillcolor="rgba(30, 144, 255, 0.22)",
                    line=dict(color="rgba(30, 100, 180, 0.8)", width=1.5),
                    name=f"Trapézio {i+1}",
                    showlegend=(i == 0),
                    hovertemplate=(
                        f"Trapézio {i+1}<br>"
                        f"x esquerdo={nos_x[i]:.4f}<br>"
                        f"x direito={nos_x[i+1]:.4f}<extra></extra>"
                    ),
                ))
        else:
            for i in range(0, n, 2):
                x_tres = nos_x[i:i+3]
                y_tres = nos_y[i:i+3]
                coef = np.polyfit(x_tres, y_tres, 2)
                xs_parabola = np.linspace(x_tres[0], x_tres[2], 100)
                ys_parabola = np.polyval(coef, xs_parabola)
                fig.add_trace(go.Scatter(
                    x=np.concatenate([xs_parabola, xs_parabola[::-1]]),
                    y=np.concatenate([ys_parabola, np.zeros_like(ys_parabola)]),
                    mode="lines", fill="toself",
                    fillcolor="rgba(255, 165, 0, 0.20)",
                    line=dict(color="rgba(190, 110, 0, 0.8)", width=1.5),
                    name=f"Parábola {i//2 + 1}",
                    showlegend=(i == 0),
                ))
                fig.add_trace(go.Scatter(
                    x=xs_parabola, y=ys_parabola, mode="lines",
                    line=dict(color="darkorange", dash="dash", width=2),
                    name="Aproximação parabólica",
                    showlegend=(i == 0),
                ))

        fig.add_trace(go.Scatter(
            x=nos_x, y=nos_y, mode="markers+text",
            text=[f"x{i}={v:.3g}" for i, v in enumerate(nos_x)],
            textposition="top center", name="Nós",
            marker=dict(size=9, color="black"),
        ))
        fig.add_hline(y=0, line_dash="dot", line_color="gray", opacity=0.7)
        fig.update_layout(
            title=f"{metodo}: visualização da aproximação",
            xaxis_title="x", yaxis_title="f(x)",
            height=600, hovermode="closest",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        )

        st.success("Integral aproximada calculada.")
        c1, c2, c3 = st.columns(3)
        c1.metric("Integral aproximada", f"{resultado:.10f}")
        c2.metric("Largura h", f"{h:.6f}")
        c3.metric("Subintervalos", n)
        st.plotly_chart(fig, use_container_width=True)

        tabela = []
        for i, (xi, yi) in enumerate(zip(nos_x, nos_y)):
            peso = "-"
            if metodo == "Trapézios repetidos":
                peso = "1" if i in (0, n) else "2"
            else:
                peso = "1" if i in (0, n) else ("4" if i % 2 else "2")
            tabela.append({"i": i, "xᵢ": xi, "f(xᵢ)": yi, "peso na fórmula": peso})
        st.subheader("Nós e valores da função")
        st.dataframe(tabela, use_container_width=True)

        if metodo == "Trapézios repetidos":
            st.latex(r"I \approx \frac{h}{2}\left[f(x_0)+2\sum_{i=1}^{n-1}f(x_i)+f(x_n)\right]")
            st.caption("Cada região sombreada é um trapézio: os lados superiores ligam dois pontos consecutivos da função.")
        else:
            st.latex(r"I \approx \frac{h}{3}\left[f(x_0)+4f(x_1)+2f(x_2)+\cdots+f(x_n)\right]")
            st.caption("Cada região sombreada é aproximada por uma parábola que passa por três nós consecutivos.")
    except Exception as erro:
        st.error(f"Não foi possível calcular a integral: {erro}")