n = int
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
        print (f'O valor digitado foi {n}')
        print ('Digite 999 para parar o programa.')
    else:
        print ('Fim do programa')
        break
print (f'Foram digitados {cont} números, e a soma entre eles é {soma}')