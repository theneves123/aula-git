#Exercício 1: Votação
#Crie um programa que pergunte a idade do usuário e confira se ele tem idade para
#votar.
#No Brasil, o voto é permitido para quem tem 16 anos ou mais.
#Use uma estrutura condicional para verificar a idade. Se for maior ou igual a
#16, exiba "Você já pode votar!".
#Caso contrário, exiba "Você ainda não tem idade para votar."


print("Você ja pode votar?")
idade = int(input(f"Informe sua idade: " ))


if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você ainda não tem idade para votar!")






