lista = [5, 2, 9, 1, 7]

esq = sorted(lista[:len(lista)//2])
dir = sorted(lista[len(lista)//2:])

resultado = []

i = j = 0

while i < len(esq) and j < len(dir):
    if esq[i] < dir[j]:
        resultado.append(esq[i])
        i += 1
    else:
        resultado.append(dir[j])
        j += 1

resultado.extend(esq[i:])
resultado.extend(dir[j:])

print(resultado)