#Exercício 13: Verificação de Ano Bissexto
#Peça ao usuário um ano (ex.: 2024).
#o Informe se ele é bissexto (divisível por 4).

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")