import numpy as np

produto_inicial = 3
deposito_inicial = 3
produto_vendido = 3
deposito_vendido = 3

matriz_estoque = []
matriz_vendidos = []

for i in range(produto_inicial):
    quantidade_inicial = []
    for j in range(deposito_inicial):
        quantidade = float(input(f"Produtos {i + 1} no depósito {j + 1}: "))
        quantidade_inicial.append(quantidade)
    matriz_estoque.append(quantidade_inicial)

matriz_np_estoque = np.array(matriz_estoque)

print("\n")

for i in range(produto_vendido):
    quantidade_vendida = []
    for j in range(deposito_vendido):
        quantidade = float(input(f"Produtos {i + 1} do depósito {j + 1} vendidos: "))
        quantidade_vendida.append(quantidade)
    matriz_vendidos.append(quantidade_vendida)

matriz_np_vendidos = np.array(matriz_vendidos)

matriz_restante = matriz_np_estoque - matriz_np_vendidos

matriz_restante[matriz_restante < 0] = 0

print("\n== Estoque inicial ==")
print(matriz_np_estoque)

print("\n== Produtos vendidos ==")
print(matriz_np_vendidos)

print("\n== Produtos restantes ==")
print(matriz_restante)

