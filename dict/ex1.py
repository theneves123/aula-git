pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "Curitiba"
}

chave = input("Digite a chave (nome, idade, cidade): ")

if chave in pessoa:
    print("Valor:", pessoa[chave])
else:
    print("Chave não encontrada.")