#Exercício 15: Simulador de Radar
#Pergunte ao usuário a velocidade de um carro.
#● Se ultrapassar 80 km/h, exiba uma mensagem dizendo que o usuário foi
#multado. A multa custa R$ 7,00 por cada km acima do limite.

velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado!")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite. Boa viagem!")