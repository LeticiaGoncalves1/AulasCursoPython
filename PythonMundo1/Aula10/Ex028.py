from random import randint
from time import sleep

pc = randint(0,5) #Faz o pc escolher um número

print ('O computador vai escolher um número entre 0 e 5, tente adivinhar...')#Jogador tenta adivinhar
print (f'*-*-'*15)
ask = int(input('Em que número eu pensei?'))
print ('PROCESSANDO...')
sleep(2)

if ask == pc:
    print ('PARABÉNS, você ganhou!')
else:
    print (f'GANHEI! Eu escolhi o número {pc} e não no número {ask}')
