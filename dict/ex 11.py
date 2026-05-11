usuarios = {}

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar usuário")
    print("2 - Remover usuário")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do usuário: ")
        idade = input("Idade: ")
        usuarios[nome] = idade
        print("Usuário adicionado!")

    elif opcao == "2":
        nome = input("Nome do usuário para remover: ")
        usuarios.pop(nome, None)
        print("Usuário removido (se existia).")

    elif opcao == "3":
        print("Usuários cadastrados:")
        for nome, idade in usuarios.items():
            print(f"{nome} - {idade}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")