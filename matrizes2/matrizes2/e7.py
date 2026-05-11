import numpy as np

matriz = np.random.randint(-1000,1000, size=(5,5))
matriz_np = np.array(matriz)

print("== Matriz ==")
print(matriz)

print(f"\nO maior número da matriz é {np.max(matriz_np)}")


