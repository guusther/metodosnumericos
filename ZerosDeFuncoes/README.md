# MÉTODOS NUMÉRICOS — ZEROS DE FUNÇÕES

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação de quatro métodos clássicos para determinação de raízes de funções em Python: Bisseção, Falsa Posição, Secante e Newton-Raphson.

## MÉTODOS IMPLEMENTADOS

- **Bisseção:** utiliza um intervalo que contém uma mudança de sinal para aproximar a raiz, dividindo-o sucessivamente ao meio.
- **Falsa Posição:** utiliza uma reta secante entre os extremos do intervalo para estimar uma aproximação da raiz.
- **Secante:** utiliza duas aproximações iniciais para construir retas secantes e encontrar novas aproximações.
- **Newton-Raphson:** utiliza a derivada da função para calcular aproximações sucessivas da raiz.

## ESTRUTURA DO PROJETO

```text
ZerosDeFuncoes/
│
├── funcoes/
│   ├── bissecao.py
│   ├── falsaposicao.py
│   ├── secante.py
│   ├── newton.py
│   └── derivada.py
│
├── main.py
├── interface.py
└── README.md
```

**Arquivos principais:**

- `funcoes/bissecao.py` — implementação do método da Bisseção.
- `funcoes/falsaposicao.py` — implementação do método da Falsa Posição.
- `funcoes/secante.py` — implementação do método da Secante.
- `funcoes/newton.py` — implementação do método de Newton-Raphson.
- `funcoes/derivada.py` — cálculo da derivada simbólica utilizada pelo método de Newton, por meio do SymPy.
- `main.py` — execução dos métodos pelo terminal, com apresentação dos históricos de iteração e geração de relatórios gráficos em HTML.
- `interface.py` — interface web desenvolvida com Streamlit, permitindo executar os métodos e visualizar tabelas e gráficos.

## COMO RODAR

1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos/ZerosDeFuncoes
```

2. Instale as dependências:

```bash
pip install streamlit plotly sympy numpy tabulate
```

3. Para iniciar a interface web:

```bash
streamlit run interface.py
```

4. Para executar a versão pelo terminal:

```bash
python main.py
```

## EXEMPLOS PARA TESTE

**Função trigonométrica**

```text
Função: cos(x) - x
Intervalo: [0, 1]
Chute inicial: 0.5
Tolerância: 0.0001
```

**Função polinomial**

```text
Função: x**3 + x - 10
Intervalo: [1, 3]
Chute inicial: 1.5
Tolerância: 0.00001
```

**Função logarítmica**

```text
Função: 1 - x*log(x)
Intervalo: [1, 2]
Chute inicial: 1.5
Tolerância: 0.0001
```

## OBSERVAÇÕES

- Os métodos de Bisseção e Falsa Posição utilizam um intervalo inicial.
- O método da Secante utiliza duas aproximações iniciais.
- O método de Newton-Raphson utiliza uma aproximação inicial e a derivada da função.
- Os métodos registram os valores obtidos durante as iterações, permitindo acompanhar a aproximação da raiz.
- A interface permite visualizar os resultados individualmente ou comparar os quatro métodos.

