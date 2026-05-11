import numpy as np

matriz = np.random.randint(-1000,1000, size=(3,3))
matriz_np = np.array(matriz)

soma = np.sum(matriz_np, axis=0)

print("\n== Matriz ==")
print(matriz_np)

print("\n== Média ==")
print(np.round(soma))


