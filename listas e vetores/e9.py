numeros = [1, 2, 2, 3, 2, 4]
cont = 0

for i in range(len(numeros)):
    if numeros[i] == 2:
        cont += 1

print(f"O número 2 aparece {cont} vezes na lista")