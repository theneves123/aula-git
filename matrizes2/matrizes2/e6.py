import numpy as np

matriz = np.random.randint(-1000,1000, size=(3,4))
matriz_np = np.array(matriz)
cont = 0

print("\n== Matriz ==")
print(matriz_np)

for i in range(matriz_np.shape[0]):
    for j in range(matriz_np.shape[1]):
        if matriz_np[i, j] % 2 == 0:
            cont += 1

print(f"\nO número de números pares na matriz é {cont}")