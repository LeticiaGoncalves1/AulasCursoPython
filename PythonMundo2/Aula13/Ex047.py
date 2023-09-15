print ('Os números pares entre 1 e 50 são: ')

for i in range (1, 51):
    if i %2 == 0: #se o número atual "índice" foi divisível por 2 e tiver o resto em 0, print.
        print (i, end = ' ')
