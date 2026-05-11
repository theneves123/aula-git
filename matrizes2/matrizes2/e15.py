import numpy as np

matriz = np.random.randint(-100,100, size=(3,3))

transposta = []

for j in range(3):
    nova_linha = []
    for i in range(3):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

rotacionada = []

for linha in transposta:
    rotacionada.append(linha[::-1])

matriz_np = np.array(matriz)
rotacionada_np = np.array(rotacionada)

print("\n== Matriz ==")
print(matriz_np)

print("\n== Rotacionada ==")
print(rotacionada_np)