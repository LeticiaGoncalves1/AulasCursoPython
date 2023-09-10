num = int(input('Digite um número inteiro: '))
print ('''Agora vamos escolher a forma de conversão desejada:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')

opção = int(input('Sua opção: '))
print ('--' * 20)

if opção == 1:
    print (f'{num} convertido para binário é {bin(num)[2:]}')
elif opção == 2:
    print (f'{num} convertido para Octal é {oct(num)[2:]}')
elif opção == 3:
    print (f'{num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção Inválida, tente novamente.')
