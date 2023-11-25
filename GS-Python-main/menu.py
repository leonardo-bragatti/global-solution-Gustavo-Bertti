from database.crud import realizar_login, cadastrar_equipe, cadastrar_nas, mostrar_nas_paciente

def menu():
    while True:
        try:
            print("\n=== Menu ===")
            print("1 -- Realizar Login")
            print("2 -- Cadastrar Equipe")
            print("3 -- Sair")

            opcao = int(input("Digite uma das opções: "))

            if opcao == 1:
                realizar_login()
                menu_secundario()
            elif opcao == 2:
                cadastrar_equipe()
            elif opcao == 3:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Não digitou uma opção válida, tente novamente")

def menu_secundario():
    while True:
        try:
            print("\n=== Menu Secundário ===")
            print("1 -- Cadastrar Nas")
            print("2 -- Mostrar Nas")
            print("3 -- Voltar para o Menu Principal")

            opcao = int(input("Digite uma das opções: "))

            if opcao == 1:
                cadastrar_nas()
            elif opcao == 2:
                id_paciente = int(input('digite o id do paciente:'))
                mostrar_nas_paciente(id_paciente)

            elif opcao == 3:
                print("Voltando para o Menu Principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Não digitou uma opção válida, tente novamente")