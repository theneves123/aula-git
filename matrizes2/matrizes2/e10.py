import numpy as np

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor do elemento [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []

for j in range(colunas):
    linha2 = []
    for i in range(linhas):
        linha2.append(matriz[i][j])
    transposta.append(linha2)

matriz_np = np.array(matriz)
transposta_np = np.array(transposta)

print("\n== Original ==")
print(matriz_np)

print("\n== Transposta ==")
print(transposta_np)
