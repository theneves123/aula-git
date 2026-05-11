dados = {
    "nome": "Ana",
    "idade": 22,
    "cidade": "Curitiba"
}

resposta = input("Deseja apagar todos os dados? (sim/não): ")

if resposta.lower() == "sim":
    dados.clear()

print("Dicionário final:", dados)