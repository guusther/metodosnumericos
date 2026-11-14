def receber_sistema():
    num_incognitas = int(input("Digite quantas incógnitas o sistema terá: "))
    termmos_independentes = int(input("Digite quantos termos independentes o sistema terá:"))
    matriz = []
    for i in range(termmos_independentes):
        linha = []
        for j in range(num_incognitas):
           coeficiente = float(input(f"Digite o coeficiente da {j + 1} incógnita:"))
           linha.append(coeficiente)
        matriz.append(linha)

    b = []
    for i in range(termmos_independentes):
        numero = float(input(f"Digite o {i}o termo indepedente:"))
        b.append(numero)

    return matriz, b