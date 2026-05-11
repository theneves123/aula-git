#Exercício 9: Classificação de Triângulos
#Peça os três lados de um triângulo ao usuário e verifique:
#● Se todos os lados forem iguais: "Equilátero".
#● Se apenas dois forem iguais: "Isósceles".
#● Se todos forem diferentes: "Escaleno".

l1 = float(input("Informe o primeiro lado: "))
l2 = float(input("Informe o segundo lado: "))
l3 = float(input("Informe o terceiro lado: "))

if l1 == l2 == l3:
    print("Triangulo Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Triangulo Isosceles")
else:
    print("Triangulo Escaleno")