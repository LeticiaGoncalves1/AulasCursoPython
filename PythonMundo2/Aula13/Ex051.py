i = int(input('Vamos fazer uma sequência de números, digite o número que deseja começar: '))

f = int(input('Até número deseja a sequência: '))

p = int(input('Escolha o intevalo que os números pularão: '))

lista =[]
contador = 0

for c in range (i, f+1, p):
    print (c)
    contador += 1
    if contador <= 10:
        lista.append(c)

print (lista)
