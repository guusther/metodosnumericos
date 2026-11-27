# MÉTODOS NUMÉRICOS — INTERPOLAÇÃO POLINOMIAL

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação de dois métodos de interpolação polinomial em Python: Interpolação por Definição e Interpolação de Newton. O projeto também conta com uma interface gráfica que permite inserir pontos, visualizar os polinômios encontrados e comparar os resultados dos métodos.

## MÉTODOS IMPLEMENTADOS

- **Interpolação por Definição:** determina os coeficientes de um polinômio interpolador por meio de um sistema linear construído a partir dos pontos informados. A matriz utilizada é a matriz de Vandermonde.
- **Interpolação de Newton:** constrói o polinômio interpolador utilizando diferenças divididas, organizadas em uma tabela para determinar seus coeficientes.

Os três métodos determinam um polinômio que passa pelos pontos fornecidos, desde que os valores de x sejam distintos.

## ESTRUTURA DO PROJETO

```text
InterpolacaoPolinomial/
│
├── interface.py
├── definicao.py
├── polinomio_newton.py
└── README.md
```

**Arquivos principais:**

- `interface.py` — interface gráfica desenvolvida com Streamlit, permitindo selecionar o método, editar os pontos conhecidos, calcular o polinômio e visualizar seu gráfico.
- `definicao.py` — implementação da interpolação por definição, com montagem da matriz de Vandermonde e resolução do sistema linear.
- `polinomio_newton.py` — implementação do método de Newton, incluindo cálculo das diferenças divididas, montagem da tabela e avaliação do polinômio.

## COMO RODAR

1. Clone o repositório e acesse a pasta principal:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Instale as dependências utilizadas pelo projeto:

```bash
pip install sympy streamlit numpy plotly pandas
```

3. Execute o método desejado pelo terminal:

**Interpolação por Definição**

```bash
python -m InterpolacaoPolinomial.definicao
```

**Interpolação de Newton**

```bash
python -m InterpolacaoPolinomial.polinomio_newton
```

4. Para executar a interface gráfica:

```bash
streamlit run InterpolacaoPolinomial/interface.py
```

## COMO UTILIZAR

### Pelo terminal

1. Informe a quantidade de pontos.
2. Digite as coordenadas x e y de cada ponto.
3. Informe o valor de x que deseja interpolar.
4. O programa apresenta o polinômio interpolador e o resultado da avaliação.

No método de Newton, também é apresentada a tabela de diferenças divididas.

### Pela interface gráfica

1. Selecione o método de interpolação desejado: Definição (Vandermonde) ou Newton.
2. Edite a tabela de pontos conhecidos, informando as coordenadas x e y.
3. Informe o valor de x no qual deseja avaliar o polinômio.
4. Clique no botão **Interpolar**.

A interface apresenta:

- O polinômio interpolador encontrado.
- O resultado da avaliação P(x).
- A quantidade de pontos utilizados.
- O gráfico do polinômio interpolador e dos pontos informados.
- A tabela de diferenças divididas, quando utilizado o método de Newton.

## OBSERVAÇÕES

- São necessários pelo menos dois pontos.
- Os valores de x devem ser distintos.
- A quantidade de pontos determina o grau máximo do polinômio interpolador.
- A implementação por definição utiliza funções da pasta `SistemasLineares` para resolver o sistema linear.
- A implementação de Newton realiza diretamente os cálculos de seu respectivo método.
- A interface gráfica utiliza Streamlit para apresentação e Plotly para geração dos gráficos.
- Para executar a interface corretamente, recomenda-se iniciar o comando a partir da pasta principal do projeto.