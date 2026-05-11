#Exercício 10: Múltiplo de 5
#Peça um número ao usuário e informe se ele é um múltiplo de 5.

md5 = float(input("Digite o valor: "))

if md5 % 5 == 0:
    print("É multiplo de 5")
else:
    print("Não é multiplo de 5")