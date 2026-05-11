import numpy as np

dias_m = 3
regiao_m   = 3
dias_t = 3
regiao_t   = 3

matriz_m = []
matriz_t = []

for i in range(dias_m):
    chuva_m = []
    for j in range(regiao_m):
        chuva = float(input(f"Chuva de manhã (mm) - Dia {i + 1}, Região {j + 1}: "))
        chuva_m.append(chuva)
    matriz_m.append(chuva_m)

matriz_np_m = np.array(matriz_m)

print("\n")

for i in range(dias_t):
    chuva_t = []
    for j in range(regiao_t):
        chuva = float(input(f"Chuva de tarde (mm) - Dia {i + 1}, Região {j + 1}: "))
        chuva_t.append(chuva)
    matriz_t.append(chuva_t)

matriz_np_t = np.array(matriz_t)

matriz_dia = matriz_np_m + matriz_np_t

print("\n")

print("\n=== Chuva Manhã ===")
print(matriz_np_m)

print("\n=== Chuva Tarde ===")
print(matriz_np_t)

print("\n=== Chuva Total ===")
print(matriz_dia)