from datetime import date
atual = date.today().year
print (f'--' * 20)
print ('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print (f'--' * 20)

nasc = int(input('Em que ano você nasceu:'))
idade = atual - nasc
print (f'Sua idade é {idade}')

if idade <= 9:
    print ('Nadador Mirim')

elif idade <= 14:
    print ('Nadador Infantil')

elif idade <= 19:
    print ('Nadador Junior')

elif idade <= 25:
    print ('Nadador Sênior')

else:
    print ('Nadador Master')