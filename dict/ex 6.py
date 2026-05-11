original = {
    "produto": "Notebook",
    "preco": 3000
}


copia = original.copy()


chave = input("Qual chave deseja alterar? (produto/preco): ")

if chave in copia:
    novo_valor = input("Digite o novo valor: ")



    if chave == "preco":
        novo_valor = float(novo_valor)

    copia[chave] = novo_valor
else:
    print("Chave não encontrada.")

print("Dicionário original:", original)
print("Dicionário cópia:", copia)