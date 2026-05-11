import numpy as np

matriz1 = np.random.randint(-100,100, size=(3,3))
matriz2 = np.random.randint(-100,100, size=(3,3))

matriz1_np = np.array(matriz1)
matriz2_np = np.array(matriz2)

mult = matriz1_np * matriz2_np

print("\n== Matriz 1 ==")
print(matriz1_np)

print("\n== Matriz 2 ==")
print(matriz2_np)

print("\n== Resultado ==")
print(mult)