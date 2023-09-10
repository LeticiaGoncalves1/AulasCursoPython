n1 = int(input('Digite o primeiro valor:'))
n2 = int (input('Digite o segundo valor:'))

maior = n1

if n2 > n1:
    maior = n2
    print (f'O segundo número é maior.')
elif n1 > n2:
    maior = n1
    print (f'O primeiro número é maior.')
elif n1 == n2:
    print ('Não existe valor maior, os dois números são iguais.')
    