numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_atual = numeros[0]
max_global = numeros[0]

for n in numeros[1:]:
    max_atual = max(n, max_atual + n)
    if max_atual > max_global:
        max_global = max_atual

print(max_global)