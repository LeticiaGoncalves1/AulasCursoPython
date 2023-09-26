# Importa as bibliotecas necessárias
from random import randint
from time import sleep

# Inicializa o contador de tentativas
contador = 0

# Inicia um loop infinito para permitir que o jogo continue até o jogador decidir parar
while True:
    # O computador escolhe um número aleatório entre 0 e 10
    pc = randint(0, 10)

    # Exibe mensagens de instrução para o jogador
    print('O computador vai escolher um número entre 0 e 10')
    print('Tente adivinhar...')
    print(f'--' * 15)
    print(' ')

    # Inicia um loop infinito para que o jogador faça várias tentativas até adivinhar o número
    while True:
        # Solicita ao jogador que insira um número e o converte para um inteiro
        ask = int(input('Em que número eu pensei? '))
        print('PROCESSANDO...')
        print(' ')
        contador += 1
        sleep(1)

        # Verifica se o número escolhido pelo jogador é igual ao número escolhido pelo computador
        if ask == pc:
            print('PARABÉNS, você ganhou!')
            break
        else:
            # Se o número for diferente, fornece dicas ("Mais" ou "Menos") e permite ao jogador tentar novamente
            if ask < pc:
                print('Mais... Tente mais uma vez.')
            elif ask > pc:
                print('Menos... Tente mais uma vez.')

    # Exibe quantas tentativas foram necessárias para o jogador vencer
    print(f'Foram necessárias {contador} vezes para você vencer!')

    # Pergunta ao jogador se ele deseja jogar novamente
    while True:
        continuar = str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            print('Comando inválido! Digite apenas S ou N.')
            continue

    # Se o jogador desejar jogar novamente, o loop externo continua; caso contrário, o jogo é encerrado
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break

# Mensagem de encerramento quando o jogador decide parar
print("PROGRAMA ENCERRADO....")
