#Exercício 16: Conversor de Temperatura
#Peça ao usuário uma temperatura em Celsius.
#● Pergunte se o ele quer converter para Fahrenheit (F) ou Kelvin (K).
#● Exiba o resultado da opção escolhida.
#Obs.: fórmula para converter de Celsius para Fahrenheit : (°C × 9/5) + 32
#fórmula para converter de Celsius para Kelvin: °C + 273,15

celsius = float(input("Digite a temperatura em Celsius: "))
opcao = input("Deseja converter para Fahrenheit (F) ou Kelvin (K)? ")

if opcao == "F":
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")
elif opcao == "K":
    kelvin = celsius + 273.15
    print(f"{celsius:.2f}°C equivalem a {kelvin:.2f}K")
else:
    print("Opção inválida. Digite F ou K.")
