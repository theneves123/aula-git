#Exercício 5: Par ou Ímpar
#Peça ao usuário que digite um número inteiro.
#● Use o operador de resto (%) para verificar se o número é par ou ímpar.
#● Exiba a mensagem correspondente.

n = int(input("Digite um valor: "))

if n % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")