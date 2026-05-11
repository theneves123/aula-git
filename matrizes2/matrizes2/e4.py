import numpy as np

matriz = np.random.randint(-1000,1000, size=(2,2))
matriz_np = np.array(matriz)

print("\n== Matriz ==")
print(matriz)

matriz_np[[0, 1]] = matriz_np[[1, 0]]

print("\n== Matriz trocada ==")
print(matriz_np)
