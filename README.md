# MÉTODOS NUMÉRICOS COMPUTACIONAIS

Trabalho desenvolvido para a disciplina de Métodos Numéricos Computacionais da Universidade Federal de Santa Maria (UFSM).

O projeto reúne implementações em Python de métodos numéricos utilizados para resolver problemas matemáticos, como sistemas lineares, interpolação de dados, ajuste de curvas, integração numérica e determinação de raízes de funções.

## ESTRUTURA DO PROJETO

```text
metodosnumericos/
│
├── AjusteCurvas/
│   ├── ajuste_polinomial.py
│   ├── interface.py
│   └── README.md
│
├── IntegracaoNumerica/
│   ├── trapezio_repetido.py
│   ├── simpson_1.py
│   └── README.md
│
├── InterpolacaoPolinomial/
│   ├── definicao.py
│   ├── lagrange.py
│   ├── polinomio_newton.py
│   └── README.md
│
├── SistemasLineares/
│   ├── eliminacao_gauss.py
│   ├── fatoracao_lu.py
│   ├── gauss_jacobi.py
│   ├── gauss_seidel.py
│   └── README.md
│
├── ZerosDeFuncoes/
│   ├── funcoes/
│   ├── main.py
│   ├── interface.py
│   └── README.md
│
└── README.md
```

Cada pasta contém as implementações relacionadas a uma área específica dos métodos numéricos. Os READMEs internos apresentam os métodos, os arquivos e as instruções particulares de execução.

## MÉTODOS IMPLEMENTADOS

**Sistemas Lineares**
- Eliminação de Gauss;
- Fatoração LU;
- Gauss-Jacobi;
- Gauss-Seidel.

**Interpolação Polinomial**
- Interpolação por definição;
- Interpolação de Lagrange;
- Interpolação de Newton.

**Ajuste de Curvas**
- Ajuste polinomial pelo método dos mínimos quadrados.

**Integração Numérica**
- Regra dos Trapézios Repetidos;
- Regra de Simpson 1/3 Repetida.

**Zeros de Funções**
- Bisseção;
- Falsa Posição;
- Secante;
- Newton-Raphson.

## TECNOLOGIAS E DEPENDÊNCIAS

O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:

- **SymPy:** manipulação de expressões matemáticas e cálculo simbólico;
- **NumPy:** operações numéricas e geração de dados para gráficos;
- **Plotly:** criação de gráficos interativos;
- **Streamlit:** desenvolvimento das interfaces web;
- **Tabulate:** organização de resultados em tabelas no terminal.

## COMO EXECUTAR

1. Clone o repositório:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Instale as dependências:

```bash
pip install streamlit plotly sympy numpy tabulate
```

3. Para executar uma implementação, consulte o README da pasta correspondente. Cada módulo possui suas próprias instruções de execução.

4. Para abrir as interfaces gráficas disponíveis:

```bash
streamlit run AjusteCurvas/interface.py
```

Para a interface de zeros de funções:

```bash
streamlit run ZerosDeFuncoes/interface.py
```

## OBSERVAÇÕES

- Os programas podem ser executados individualmente, conforme as instruções de cada pasta.
- As interfaces gráficas estão disponíveis para os métodos de ajuste de curvas e zeros de funções.
- Os demais métodos possuem execução pelo terminal.
- Os módulos compartilham funções quando necessário, evitando a repetição de implementações.

---

Trabalho acadêmico — Métodos Numéricos Computacionais  
Universidade Federal de Santa Maria (UFSM)