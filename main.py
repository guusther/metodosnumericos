from funcoes.bissecao import bissecao
from funcoes.falsaposicao import falsa_posicao
from funcoes.secante import secante
from funcoes.newton import newton

import plotly.graph_objects as go
import numpy as np

def funcao(x):
    return x**3 - x - 2

hist_bissecao = bissecao(1, 2, funcao, 0.01)
hist_falsa = falsa_posicao(1, 2, funcao, 0.01)
hist_secante= secante(1, 2, funcao, 0.01)
hist_newton = newton(2, funcao, 0.01)

#parte do grafico
x_vals = np.linspace(1, 2, 200)
y_vals = [funcao(x) for x in x_vals]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", name="f(x)"))

metodos = {
    "Bisseção": hist_bissecao,
    "Falsa Posição": hist_falsa,
    "Secante": hist_secante,
    "Newton": hist_newton,
}

for nome, historico in metodos.items():
    fig.add_trace(go.Scatter(x=[p["x"] for p in historico], y=[p["fx"] for p in historico],
                             mode="markers+lines", name=nome))

fig.update_layout(
    title="Convergência dos métodos de zero de função",
    xaxis_title="x",
    yaxis_title="f(x)"
)

fig.write_html("relatorio.html", auto_open=True)