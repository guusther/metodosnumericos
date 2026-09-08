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

"""
linspace significa tipo: de 200 numeros entre 1 e 2 basicamente. Então se
no lugar do 200 fosse 5 seria algo do tipo [1.0, 1.25, 1.5, 1.75, 2]
Entretanto, ser 200 numeros faz com que a distancia seja bem menor q 0.25, portanto, quando o
grafico for desenhado, será uma linha continua ao inves de pontos separados
"""

y_vals = [funcao(x) for x in x_vals]

"""
isso aqui eh a mesma coisa de um for com .append. Ele vai
calcular funcao(x) para cada um dos 200 e guardar numa lista
"""

fig = go.Figure()

"""
fig inicialmente eh uma tela em branco que ao decorrer vai sendo empilhada com 
camadas de desenho

o go.Scatter cria uma camada de desenho. Ela recebe duas listas paralelas, sendo
nesse caso as listas dos valore de x e y. mode="lines" é pra ligar esses pontos 
com uma linha e o name é o texto que aparece na legenda do gráfico
"""
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", name="f(x)"))


"""

"""
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