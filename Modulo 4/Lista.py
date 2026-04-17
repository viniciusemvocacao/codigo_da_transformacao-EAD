compras = ['Leite', 'Pão', 'Ovos']

while compras != 4:
    print('== Lista de compras🛒')
    print('1. Ver lista')
    print('2. Adicionar itens')
    print('3. Remover itens')
    print('4. Sair')
    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        print(f'{compras}')
    elif escolha == 2:
        item = input('Digite o item a ser adicionado: ')
        compras.append(item)
        print(f'{item} adicionado à lista.')
    elif escolha == 3:
        item = input('Digite o item a ser removido: ')
        if item in compras:
            compras.remove(item)
            print(f'{item} removido da lista.')
    elif escolha == 4:
        print('Saindo...') 
        break
    else:
        print('Opção inválida. Tente novamente.')       
    

   