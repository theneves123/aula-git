import numpy as np

matriz = []

for i in range(3):
    linha=[]
    for j in range(3):
        valor = float(input(f"Digite o número da posição [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

matriz_np = np.array(matriz)

soma = np.sum(matriz_np)

print("== Soma ==")
print(soma)