n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print (f'Seu primeiro nome é {nome[0]}')
print ('Seu último nome é {}'.format(nome[len(nome)-1]))