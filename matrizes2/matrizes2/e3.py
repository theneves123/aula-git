import numpy as np

matriz = np.random.randint(-10,10, size=(3,3))
matriz_np = np.array(matriz)

n = int(input("Digite um número inteiro entre -10 e 10: "))

print(matriz_np)

if n in matriz_np:
    print("\nSeu número está presente na matriz")
else:
    print("\nSeu número não está presente na matriz")