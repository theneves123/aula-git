#Exercício 17: Loja de Tintas
#Peça o tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros (R$ 80,00). Informe ao usuário se ele precisa de apenas uma
#lata ou mais de uma.

area = float(input("Digite o tamanho da área em metros quadrados: "))

litros_necessarios = area / 3

if litros_necessarios % 18 == 0:
    latas_necessarias = int(litros_necessarios / 18)
else:
    latas_necessarias = int(litros_necessarios / 18) + 1

preco = latas_necessarias * 80

if latas_necessarias == 1:
    print("Você precisa de 1 lata de tinta.")
else:
    print(f"Você precisa de {latas_necessarias} latas de tinta.")

print(f"Preço total: R$ {preco:.2f}")