# MÉTODOS NUMÉRICOS — AJUSTE DE CURVAS

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação do método dos mínimos quadrados para realizar ajustes polinomiais em conjuntos de pontos, utilizando Python.

## MÉTODO IMPLEMENTADO

**Ajuste Polinomial pelo Método dos Mínimos Quadrados**

O método dos mínimos quadrados determina um polinômio que representa uma aproximação dos pontos fornecidos. Diferentemente da interpolação, o polinômio não precisa passar exatamente por todos os pontos: seus coeficientes são calculados de modo a minimizar a soma dos quadrados dos resíduos.

A implementação monta o sistema de equações normais e utiliza a Eliminação de Gauss para determinar os coeficientes do polinômio.

## ESTRUTURA DO PROJETO

```text
AjusteCurvas/
│
├── ajuste_polinomial.py
├── interface.py
└── README.md
```

**Arquivos principais:**

- `ajuste_polinomial.py` — implementação do ajuste polinomial, incluindo leitura dos pontos, montagem da matriz das equações normais, validação dos dados e cálculo do polinômio.
- `interface.py` — interface web desenvolvida com Streamlit, permitindo informar os pontos, escolher o grau do polinômio, visualizar os coeficientes, calcular valores e gerar o gráfico do ajuste.

## COMO RODAR

1. Clone o repositório e acesse a pasta principal:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Instale as dependências:

```bash
pip install streamlit plotly numpy
```

3. Inicie a interface web:

```bash
streamlit run AjusteCurvas/interface.py
```

## COMO UTILIZAR

1. Informe a quantidade de pontos que serão utilizados.
2. Preencha as coordenadas x e y de cada ponto.
3. Escolha o grau desejado para o polinômio.
4. Clique em **Calcular ajuste**.
5. Visualize o polinômio encontrado, seus coeficientes, o erro total quadrático e o gráfico.
6. Informe um valor de x para avaliar o polinômio nesse ponto.

## OBSERVAÇÕES

- A quantidade de pontos deve ser suficiente para o grau escolhido: são necessários pelo menos `grau + 1` pontos.
- A implementação também verifica a quantidade de valores de x distintos.
- O método utiliza a Eliminação de Gauss, implementada na pasta `SistemasLineares`, para resolver o sistema de equações normais.

