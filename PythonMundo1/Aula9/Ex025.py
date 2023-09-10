nome = str(input('Digite seu nome completo: '))
nome1 = nome.strip().lower()
print (nome)
print ('Seu nome tem Silva? {}'.format('silva' in nome1))