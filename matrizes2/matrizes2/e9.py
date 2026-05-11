import numpy as np

matriz = np.random.randint(-100, 100, size=(4,4))
matriz_np = np.array(matriz)

soma = 0

for i in range(4):
    for j in range(4):
        if i == j:
            soma += matriz[i, j]

print("\n== Matriz ==")
print(matriz_np)

print("\n== Soma ==")
print(soma)