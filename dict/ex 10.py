dados = {
    "nome": "Ana",
    "idade": 22,
    "cidade": "Curitiba"
}


chave = input("Qual chave deseja remover? ")

dados.pop(chave, None)

dados.popitem()

print("Após remoções:", dados)

nova_chave = input("Digite uma nova chave: ")
novo_valor = input("Digite o valor: ")

dados.update({nova_chave: novo_valor})

print("Dicionário final:", dados)