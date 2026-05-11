#Exercício 2: Positivo, Negativo ou Zero
#Crie um programa que peça um número inteiro ao usuário.
# Se o número for maior que zero, exiba a mensagem: "O número X é Positivo."
# Se o número for menor que zero, exiba: "O número X é negativo."
# Senão, exiba: "O número é Zero."

nint = int(input("Escreva um valor inteiro: "))

if nint > 0:
        print(f"O número {nint} é Positivo")
elif nint < 0:
        print(f"O número {nint} é negativo")
else:
        print("O número é Zero")