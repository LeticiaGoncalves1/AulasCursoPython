somaPar = 0
somaImpar = 0
cont = 0

for c in range (1, 7):
    n = int(input('Digite um número:'))
    if n %2 == 0:
        somaPar += n
    if n %2 != 0:
        somaImpar += n
    cont += 1
    print (f'número {cont}')
    print (' ')

print ('--' * 20)
print (f'Soma números pares é igual a {somaPar}.')
print (f'Soma dos números impares é igual a {somaImpar}')
