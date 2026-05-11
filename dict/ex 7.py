nomes = input("Digite nomes separados por vírgula: ").split(",")

nomes = [nome.strip() for nome in nomes]

dicionario = dict.fromkeys(nomes, 0)

print("Dicionário:", dicionario)