print ('--' * 20)
print ('Verificador de triângulos')
print ('--' * 20)

n1 = float(input('Digite o valor da primeira reta:'))
n2 = float(input('Digite o valor da segunda reta:'))
n3 = float (input('Digite o valor da terceira reta:'))

if n1 < n2 + n3 and  n2 < n1 + n3 and n3 < n1 + n2:
    print('Isso forma um triângulo ' , end='')
    if n1 == n2 == n3:
        print ('Equilátero')
    elif n1 != n2 != n3 != n1:
        print ('Escaleno')
    #elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2:
        #print ('Isósceles') #PODE FAZER DE FORMA SIMPLIFICADA!
    else:
        print ('Isósceles')

else:
    print ('Não forma um triângulo')