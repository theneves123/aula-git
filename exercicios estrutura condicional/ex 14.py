#Exercício 14: Aumento Salarial
#Peça o salário de um funcionário.
#● Se o salário for superior a R$ 1.621,00, calcule um aumento de 10%.
#● Para inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário: R$ "))

if salario > 1621:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"Novo salário: R$ {novo_salario:.2f}")