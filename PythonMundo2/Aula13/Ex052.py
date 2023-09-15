print ('--- Verificador de números primos ---')
n = int(input('Digite um número: '))

total = 0

for c in range (1, n + 1):
    if n % c == 0:
        print ('\033[33m', end = ' ')
        #cógido da cor vermelha.
        total += 1
    else:
        print ('\033[31m', end = ' ')
        #código da cor amarela.
    print (f'{c}', end = ' ')

print (f'\n\033[m0 número {n} foi divisivel {total} vezes.')
if total == 2:
    print ('E por isso ele É PRIMO.')
else:
    print ('E por isso ele NÃO É PRIMO.')
