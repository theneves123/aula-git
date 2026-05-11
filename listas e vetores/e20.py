def permutar(lista):
    if len(lista) == 0:
        return [[]]

    resultado = []

    for i in range(len(lista)):
        elemento = lista[i]
        resto = lista[:i] + lista[i+1:]

        for p in permutar(resto):
            resultado.append([elemento] + p)

    return resultado

print(permutar([1, 2, 3]))