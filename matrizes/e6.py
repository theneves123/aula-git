import numpy as np

matriz = np.random.randint(-1000, 1000, size=(4, 4))

matriz_np = np.array(matriz)

print("\n== Matriz inicial ==")
print(matriz_np)

matriz_np.fill(1)

print("\n== Matriz ativa ==")
print(matriz_np)