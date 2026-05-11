#Exercício 11: Categorias de Atleta
#Solicite a idade de um nadador e classifique-o:
#● 5 a 7 anos: Infantil A.
#● 8 a 10 anos: Infantil B.
#● 11 a 13 anos: Juvenil A.
#● 14 a 17 anos: Juvenil B.
#● Maiores de 18: Adulto.

idade = int(input("Qual a sua idade? " ))

if idade <= 5:
    print("Não tem idade suficiente")
elif idade <= 7:
    print("Infantil A")
elif idade <= 10:
    print("Infantil B")
elif idade <= 13:
    print("Juvenil A")
elif idade <= 17:
    print("Juvenil B")
else:
    print("Adulto")


