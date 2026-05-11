#Exercício 7: Verificação de Login
#Crie uma variável chamada usuario_correto com o valor "admin".
#● Peça para o usuário digitar um nome de usuário.
#● Se for igual ao armazenado, exiba "Acesso concedido".
#● Caso contrário, "Usuário desconhecido".

usuario_correto = "admin"

input("Digite um nome de usuário: ")
if usuario_correto == "admin":
    print("Acesso concedido")
else:
    print("Usuário desconhecido")