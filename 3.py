
matriz = []


for i in range(0, 10):
    linha = []

    for i in range(0, 10):
        linha.append(int(input("Digite um número do seu teclado:")))
    matriz.append(linha)

for i in range(0, 10):
    print(matriz[i])
