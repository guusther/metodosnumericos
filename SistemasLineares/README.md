# MÉTODOS NUMÉRICOS — SISTEMAS LINEARES

Trabalho da disciplina de Métodos Numéricos Computacionais (UFSM).

Implementação de quatro métodos numéricos para resolução de sistemas de equações lineares em Python: Eliminação de Gauss, Fatoração LU, Gauss-Jacobi e Gauss-Seidel.

## MÉTODOS IMPLEMENTADOS

- **Eliminação de Gauss:** transforma a matriz aumentada do sistema em uma matriz triangular superior por meio de operações elementares entre linhas. Em seguida, utiliza substituição retroativa para encontrar as incógnitas.
- **Fatoração LU:** decompõe a matriz dos coeficientes em matrizes triangulares inferior e superior. A implementação utiliza pivoteamento e matriz de permutação.
- **Gauss-Jacobi:** método iterativo que calcula novas aproximações das incógnitas utilizando exclusivamente os valores da iteração anterior.
- **Gauss-Seidel:** método iterativo que utiliza imediatamente os valores atualizados durante cada iteração.

## ESTRUTURA DO PROJETO

```text
SistemasLineares/
│
├── eliminacao_gauss.py
├── fatoracao_lu.py
├── gauss_jacobi.py
├── gauss_seidel.py
├── main.py
└── README.md
```

**Arquivos principais:**

- `eliminacao_gauss.py` — implementação da eliminação de Gauss, incluindo montagem da matriz aumentada, pivoteamento e substituição retroativa.
- `fatoracao_lu.py` — implementação da fatoração LU, com matrizes L, U e P, além das substituições progressiva e regressiva.
- `gauss_jacobi.py` — implementação do método iterativo de Gauss-Jacobi.
- `gauss_seidel.py` — implementação do método iterativo de Gauss-Seidel.
- `main.py` — arquivo reservado para o ponto de entrada do projeto.

## COMO RODAR

1. Clone o repositório e acesse a pasta principal:

```bash
git clone https://github.com/guusther/metodosnumericos
cd metodosnumericos
```

2. Não é necessário instalar bibliotecas externas para executar os métodos desta pasta. As implementações utilizam recursos da biblioteca padrão do Python.

3. Execute o método desejado pelo terminal:

**Eliminação de Gauss**

```bash
python SistemasLineares/eliminacao_gauss.py
```

**Fatoração LU**

```bash
python SistemasLineares/fatoracao_lu.py
```

**Gauss-Jacobi**

```bash
python SistemasLineares/gauss_jacobi.py
```

**Gauss-Seidel**

```bash
python SistemasLineares/gauss_seidel.py
```

## OBSERVAÇÕES

- Os programas solicitam os coeficientes das equações e os termos independentes do sistema.
- A Eliminação de Gauss e a Fatoração LU utilizam pivoteamento parcial.
- Os métodos de Gauss-Jacobi e Gauss-Seidel utilizam aproximações iniciais iguais a zero.
- Os métodos iterativos utilizam tolerância de `0.0001` e limite de 1000 iterações.
- Os métodos iterativos podem não convergir para todos os sistemas.

