pares = []

for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor {i+1}: ")
    pares.append((chave, valor))

dicionario = dict(pares)

print("Dicionário:", dicionario)