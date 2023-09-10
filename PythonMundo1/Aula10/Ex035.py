print (f'*' * 10)
print ('ANALISADOR DE TRIANGULOS')
print (f'*' * 10)

n1 = float(input('Digite o valor da primeira reta:'))
n2 = float(input('Digite o valor da segunda reta:'))
n3 = float(input('Digite o valor da terceira reta:'))
print ('VERIFICANDO SE FORMAM UM TRIANGULO...')

if n1 < n2 + n3 and  n2 < n1 + n3 and n3 < n1 + n2:
    print ('Isso forma um triangulo')
else:
    print ('Não forma um triangulo')