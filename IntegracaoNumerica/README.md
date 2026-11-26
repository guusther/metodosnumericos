# MÉTODOS NUMÉRICOS — INTEGRAÇÃO NUMÉRICA

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação de dois métodos de integração numérica em Python: Regra dos Trapézios Repetidos e Regra de Simpson 1/3 Repetida.

## MÉTODOS IMPLEMENTADOS

- **Regra dos Trapézios Repetidos:** aproxima o valor da integral definida dividindo o intervalo de integração em vários subintervalos e aproximando a área sob a curva por meio de trapézios.
- **Regra de Simpson 1/3 Repetida:** aproxima o valor da integral definida utilizando parábolas para representar a função em grupos de subintervalos.

Os dois métodos recebem uma função matemática e os limites de integração, calculando uma aproximação numérica para a integral.

## ESTRUTURA DO PROJETO

```text
IntegracaoNumerica/
│
├── trapezio_repetido.py
├── simpson_1.py
└── README.md
```

**Arquivos principais:**

- `trapezio_repetido.py` — implementação da Regra dos Trapézios Repetidos, incluindo leitura da função, cálculo do espaçamento entre os pontos e soma das contribuições dos subintervalos.
- `simpson_1.py` — implementação da Regra de Simpson 1/3 Repetida, incluindo validação da quantidade de subintervalos e aplicação dos pesos correspondentes a cada ponto.

## COMO RODAR

1. Clone o repositório e acesse a pasta principal:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Instale a dependência:

```bash
pip install sympy
```

3. Execute o método desejado:

**Regra dos Trapézios Repetidos**

```bash
python IntegracaoNumerica/trapezio_repetido.py
```

**Regra de Simpson 1/3 Repetida**

```bash
python IntegracaoNumerica/simpson_1.py
```

## COMO UTILIZAR

1. Informe o limite inferior da integração.
2. Informe o limite superior da integração.
3. Digite a função matemática utilizando a variável `x`.
4. Informe a quantidade de subintervalos.
5. O programa apresenta o valor aproximado da integral.

**Exemplos de funções:**

```text
x**2
x**3 - x - 2
sin(x)
cos(x)
log(x)
sqrt(x)
```

## OBSERVAÇÕES

- A função deve ser digitada utilizando a sintaxe matemática aceita pelo SymPy.
- A quantidade de subintervalos deve ser um número inteiro positivo.
- No método de Simpson 1/3 Repetido, a quantidade de subintervalos também deve ser par.
- A quantidade de subintervalos determina o espaçamento entre os pontos utilizados na aproximação da integral.

