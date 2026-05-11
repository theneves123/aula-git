#Exercício 18: Aprovação de Empréstimo
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma
#casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai
#pagar. A prestação mensal não pode exceder 30% do salário ou o empréstimo será
#negado.

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Em quantos anos pretende pagar? "))

meses = anos * 12
prestacao = valor_casa / meses

limite = salario * 0.3

print(f"Prestação mensal: R$ {prestacao:.2f}")
print(f"Limite permitido (30% do salário): R$ {limite:.2f}")

if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")

    #Os ex 1, 3, 5, 7, 8, 10, 12, 13, 14, 15
    #são Estruturas condicionais compostas pois utilizam apenas de um condicao
    #falsa e outra verdadeira
    #Já os ex restantes são Estruturas condicionais aninhadas
    #pois utilizam de uma condicao dentro da outras, ou seja,
    #uma decisao depende de outra decisão.