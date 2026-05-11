import numpy as np

tamanho = int(input("Digite o tamanho da matriz: "))
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        valor = int(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

matriz_np = np.array(matriz)

simetrica = True

for i in range(tamanho):
    for j in range(tamanho):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("\n== Matriz ==")
    print(matriz_np)

    print("\nA matriz é simétrica")
else:
    print("\n== Matriz ==")
    print(matriz_np)

    print("\nA matriz é assimétrica")