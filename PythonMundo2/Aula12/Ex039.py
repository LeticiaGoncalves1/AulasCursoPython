from datetime import date
atual = date.today().year
nasc = int(input('Em qual ano você nasceu? '))
idade = atual - nasc

print (f'Quem nasceu em {nasc} tem {idade} anos.')

if idade ==  18:
    print ('Está na hora de se alistar.')
    
if idade <  18:
    saldo = 18 - idade
    ano = atual + saldo
    print (f'Você ainda não tem 18 anos, ainda faltam {saldo} anos para o alistammento.')
    print (f'Seu alistamento será em {ano}.')

if idade > 18:
    saldo = idade - 18
    print (f'Você já já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print (f'Seu alistamento foi em {ano}.')
