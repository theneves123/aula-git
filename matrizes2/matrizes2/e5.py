import numpy as np

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o elemento da posição [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)
matriz_np = np.array(matriz)

n = float(input("\nDigite o número para multiplicar: "))

resultado = matriz_np * n
print(resultado)
