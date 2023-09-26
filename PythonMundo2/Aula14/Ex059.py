# Solicita ao usuário que digite dois números inteiros
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

# Inicia um loop infinito com 'while True'
while (True):
    # Exibe um menu de opções para o usuário
    print ('Selecione o que deseja fazer: ')
    escolha = int(input('''
    [ 1 ] somar
    [ 2 ] para multiplicar
    [ 3 ] maior
    [ 4 ] para escolher novos valores
    [ 5 ] para sair do programa
    Digite aqui: '''))
    print (' ')
    
    # Verifica a escolha do usuário com base no número digitado
    if escolha == 1:
        print (f'A soma entre {n1} + {n2} = {n1 + n2}')
        print('-'*40)

    if escolha == 2:
        print (f'A multiplicação de {n1} por {n2} é igual a {n1 * n2}')
        print('-'*40)

    if escolha == 3:
        # Verifica qual número é maior ou se são iguais
        if n2 > n1:
            maior = n2
            menor = n1
            print (f'{maior} é maior que {menor}.')
            print('-'*40)
        elif n1 > n2:
            maior = n1
            menor = n2
            print (f'{maior} é maior que {menor}')
        else:
            print ('Não há maior ou menor, ambos são iguais.')

    if escolha == 4:
        # Permite ao usuário escolher novos valores para n1 e n2
        print ('Informe os números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('-'*40)

    if escolha == 5:
        # Sai do programa se o usuário escolher a opção 5
        break
