import numpy as np

matriz = np.random.randint(-1000, 1000, size=(5, 5))

matriz_np = np.array(matriz)

print("\n== Matriz inicial ==")
print(matriz_np)

matriz_np[0, 1] = 6
matriz_np[2, 4] = 7

print("\n== Matriz atualizada ==")
print(matriz_np)