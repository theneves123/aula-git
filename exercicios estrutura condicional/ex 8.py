#Exercício 8: Calculadora de IMC Simples
#Peça o peso e a altura do usuário.
#● Calcule o IMC ($peso / altura^2$).
#● Se o IMC for maior que 25, exiba "Acima do peso ideal".
#● Caso contrário, exiba "Peso dentro da normalidade".

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / altura**2

if imc >= 25:
    print("Acima do peso ideal")
else:
    print("Peso dentro da normalidade")

