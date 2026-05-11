#Exercício 6: Comparando Dois Números
#Peça dois números ao usuário.
#● O programa deve informar qual deles é o maior.
#● Caso sejam iguais, o programa também precisará informar.

n1 = float(input("Digite o valor do primeiro numero: "))
n2 = float(input("Digite o valor do segundo numero: "))

if n1 > n2:
    print(f"O número {n1} é maior")
elif n1 == n2:
    print("Os dois número são iguais")
else:
    print(f"O número {n2} é maior")