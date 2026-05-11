lista = [1, 2, 3, 4, 5]
n = 2

n = n % len(lista)

rotacionada = lista[-n:] + lista[:-n]

print(rotacionada)