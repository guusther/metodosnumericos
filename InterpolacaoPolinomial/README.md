# MÉTODOS NUMÉRICOS — INTERPOLAÇÃO POLINOMIAL

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação de três métodos de interpolação polinomial em Python: Interpolação por Definição, Interpolação de Lagrange e Interpolação de Newton.

## MÉTODOS IMPLEMENTADOS

- **Interpolação por Definição:** determina os coeficientes de um polinômio interpolador por meio de um sistema linear construído a partir dos pontos informados. A matriz utilizada é a matriz de Vandermonde.
- **Interpolação de Lagrange:** constrói o polinômio interpolador utilizando uma combinação de polinômios básicos de Lagrange.
- **Interpolação de Newton:** constrói o polinômio interpolador utilizando diferenças divididas, organizadas em uma tabela para determinar seus coeficientes.

Os três métodos determinam um polinômio que passa pelos pontos fornecidos, desde que os valores de x sejam distintos.

## ESTRUTURA DO PROJETO

```text
InterpolacaoPolinomial/
│
├── definicao.py
├── lagrange.py
├── polinomio_newton.py
└── README.md
```

**Arquivos principais:**

- `definicao.py` — implementação da interpolação por definição, com montagem da matriz de Vandermonde e resolução do sistema linear.
- `lagrange.py` — implementação do polinômio interpolador de Lagrange, incluindo cálculo e formatação do polinômio.
- `polinomio_newton.py` — implementação do método de Newton, incluindo cálculo das diferenças divididas, montagem da tabela e avaliação do polinômio.

## COMO RODAR

1. Clone o repositório e acesse a pasta principal:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Instale as dependências utilizadas pelo projeto:

```bash
pip install sympy
```

3. Execute o método desejado:

**Interpolação por Definição**

```bash
python -m InterpolacaoPolinomial.definicao
```

**Interpolação de Lagrange**

```bash
python -m InterpolacaoPolinomial.lagrange
```

**Interpolação de Newton**

```bash
python -m InterpolacaoPolinomial.polinomio_newton
```

## COMO UTILIZAR

1. Informe a quantidade de pontos.
2. Digite as coordenadas x e y de cada ponto.
3. Informe o valor de x que deseja interpolar.
4. O programa apresenta o polinômio interpolador e o resultado da avaliação.

No método de Newton, também é apresentada a tabela de diferenças divididas.

## OBSERVAÇÕES

- São necessários pelo menos dois pontos.
- Os valores de x devem ser distintos.
- A quantidade de pontos determina o grau máximo do polinômio interpolador.
- A implementação por definição utiliza funções da pasta `SistemasLineares` para resolver o sistema linear.
- As implementações de Lagrange e Newton realizam diretamente os cálculos de seus respectivos métodos.

