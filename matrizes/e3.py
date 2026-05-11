import numpy as np

ingredientes = 3
lanches_i = 2
pedidos = 3
lanches_p = 2

matriz_ingredientes = []
matriz_pedidos = []

for i in range(lanches_i):
    quantidade_ingredientes = []
    for j in range(ingredientes):
        ingrediente = int(input(f"Lanche {i+1}, ingrediente {j+1}: "))
        quantidade_ingredientes.append(ingrediente)
    matriz_ingredientes.append(quantidade_ingredientes)

matriz_np_ingredientes = np.array(matriz_ingredientes)

print("\n")

for i in range(pedidos):
    quantidade_pedidos = []
    for j in range(lanches_p):
        pedido = int(input(f"Digite o número de pedidos do cliente {i+1} do lanche {j+1}: "))
        quantidade_pedidos.append(pedido)
    matriz_pedidos.append(quantidade_pedidos)

matriz_np_pedidos = np.array(matriz_pedidos)

matriz_final = np.dot(matriz_np_ingredientes, matriz_np_pedidos)

print("\n== Ingredientes por cliente ==")
print(matriz_final)



