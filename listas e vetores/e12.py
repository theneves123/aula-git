numeros = [3, 7, 1, 9, 2, 5]

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print("Maior:", maior)
print("Menor:", menor)