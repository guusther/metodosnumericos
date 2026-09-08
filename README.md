METODOS NUMERICOS - ZERO DE FUNCAO
====================================

Trabalho da disciplina de Metodos Numericos Computacionais (UFSM).
Implementacao dos 4 metodos classicos de zero de funcao em Python:
Bissecao, Falsa Posicao, Secante e Newton-Raphson.


ESTRUTURA DO PROJETO
---------------------
funcoes/            - implementacao de cada metodo, um arquivo por metodo

funcoes/derivada.py  - calculo de derivada simbolica (usado por Newton, via sympy)

main.py              - ponto de entrada: chama os 4 metodos e gera o relatorio grafico


COMO RODAR
-----------
1. Instalar as dependencias (Python 3 e pip precisam estar instalados):

   pip install -r requirements.txt

2. Rodar o programa:

   python main.py

Isso executa os 4 metodos sobre f(x) = x^3 - x - 2 no intervalo [1, 2],
e gera um arquivo relatorio.html com um grafico interativo (zoom, hover)
comparando a convergencia de cada metodo. O arquivo abre automaticamente
no navegador.


TRATAMENTO DE ERRO
--------------------
Bissecao e Falsa Posicao verificam se ha troca de sinal no intervalo
antes de iniciar. Newton e Secante verificam divisao por zero (derivada
nula / diferenca de f(x) nula) durante a execucao.