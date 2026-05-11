import numpy as np

n = int(input("Digite o tamanho da matriz: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
matriz_np = np.array(matriz)

print("== Matriz identidade ==")
print(matriz_np)