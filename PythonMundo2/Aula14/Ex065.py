soma = 0
media = 0
contador = 0

while True:
    n = int(input('Digite um valor: '))
    contador = contador + 1
    soma = soma + n
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print (' ')
    if continuar == 'S':
        print (f'Você digitou {contador} números.')
        print (' ')
        continue
    else:
        break

media = soma / contador
print (soma, media)