agenda = {}

while True:
    print("\n=== Agenda de Contatos ===")
    print("1. Adicionar | 2. Remover | 3. Buscar | 4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso!")
    elif opcao == "2":
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in agenda:
            agenda.pop(nome)
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print(f"Contato '{nome}' não encontrado na agenda.")
    elif opcao == "3":
        nome = input("Digite o nome do contato a ser buscado: ")
        if nome in agenda:
            print(  f"Contato encontrado: {nome} - {agenda[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado na agenda.")
    elif opcao == "4":
        print("Encerrando a agenda. Até mais!")
        break