import numpy as np

matriz = np.random.randint(-1000, 1000, size=(3, 3))

matriz_np = np.array(matriz)

print("\n== Matriz inicial ==")
print(matriz_np)

matriz_np.fill(0)

print("\n== Matriz zerada ==")
print(matriz_np)