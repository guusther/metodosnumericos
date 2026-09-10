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

interface.py - mesma coisa que o main, porém com interface web.


COMO RODAR
-----------
1. Clone o repositório e acesse a pasta
```bash 
git clone https://github.com/guusther/metodosnumericos

cd metodosnumericos
```

2. Instale as dependências
```bash
pip install streamlit plotly sympy numpy tabulate
```
3. Inicie o Servidor Local
```bash
streamlit run interface.py
```
Exemplos para teste
--------------------
Trigonométrica: cos(x) - x | Intervalo: [0, 1] | Chute inicial: 0.5 | Tolerância: 0.0001

Polinomial: x**3 + x - 10 | Intervalo: [1, 3] | Chute inicial: 1.5 | Tolerância: 0.00001

Logarítmica: 1 - x*log(x) | Intervalo: [1, 2] | Chute inicial: 1.5 | Tolerância: 0.0001
