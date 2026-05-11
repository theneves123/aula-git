# 3: O Desconto do Cliente
#Peça ao usuário que digite o valor total de uma compra (use float() ).
#● Se o valor da compra for maior que R$ 100.00, aplique um desconto de 10% e
#mostre o valor final a ser pago.
#● Se for menor ou igual a R$ 100.00, o cliente não ganha desconto. Exiba o
#valor normal da compra e uma mensagem: "Nas compras acima de R$ 100,
# ganha 10% de desconto!".

valor = float(input("informe o valor da compra: R$"))
desconto = valor - 10% valor

if valor >= 100:
    print("Você ganhou um desconto de 10%")
    print(f"O valor da compra ficara: R${desconto}")
else:
    print(f"O valor da compra ficou R${valor}")
    print("Nas compras acima de R$100, você ganha 10% de desconto!")
