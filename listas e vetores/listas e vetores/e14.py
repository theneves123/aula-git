numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impar = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        impar += 1

print(impar)