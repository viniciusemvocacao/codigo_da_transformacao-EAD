opcao = ''

while opcao != '3':
    print('=== Escolha uma opção ===')
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')
    opcao = input('Digite sua escolha: ')

    if opcao == '1':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 + num2
        print(f'O resultado da soma é: {resultado}')
    elif opcao == '2':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 - num2
        print(f'O resultado da subtração é: {resultado}')
    elif opcao == '3':
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')