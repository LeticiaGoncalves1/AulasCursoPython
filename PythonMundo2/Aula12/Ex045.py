from random import randint
from time import sleep

itens = ('pedra✊', 'papel✋', 'tesoura✌️')
computador = randint (0, 2)

print ('Vamos jogar Jo-Ken-Pô!')
print ('-' * 30)
print ('''Suas opções:
[ 0 ] pedra✊
[ 1 ] papel✋
[ 2 ] tesoura✌️
Escolha o seu: ''')

jogador = int(input('Qual a sua jogada? '))
sleep (2)

print ('-' * 30)
print (f'O jogador jogou {itens[jogador]} .')
print (f'O computador escolheu {itens[computador]} .')
print ('-' * 30)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print ('Empate, pedra com pedra.')
    elif jogador == 1:
        print ('Você ganhou! Papel ganha de pedra.')
    elif jogador == 2:
        print ('O computador ganhou! Pedra ganha de tesoura.')
    else:
        print ('Jogada Inválida.')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print ('O computador ganhou! Papel ganha de pedra.')
    elif jogador == 1:
        print ('Empate. Papel com papel.')
    elif jogador == 2:
        print ('Você ganhou! Tesoura ganha de papel.')
    else:
        print ('Jogada Inválida.')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print ('Você ganhou! Pedra ganha de tesoura.')
    elif jogador == 1:
        print ('O computador ganhou! Tesoura ganha de papel.')
    elif jogador == 2:
        print ('Empate, tesoura com tesoura.')
    else:
        print ('Jogada Inválida.')

print ('-' * 30)
