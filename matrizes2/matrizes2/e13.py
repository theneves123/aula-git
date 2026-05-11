import numpy as np

matriz = np.random.randint(-1000,1000, size=(5,5))
matriz_np = np.array(matriz)

print("\n== Matriz ==")
print(matriz_np)

for i in range(5):
    print(matriz_np[i, 5-1-i])