#n= int(input(' Digite um número: '))
#for c in range (0, n+1):
#    print (c) #printa de 0 até o número selecionado.
#print ('fim da contagem.')

#print ('-' * 20)

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))

#são selecionados os valores de início e fim, e a quantidade de números que serão pulados.

#
#for c in range (i, f+1, p):
#    print (c) 
#print ('fim')

#print ('-' * 20)

s = 0 
for c in range (0, 4): #pede um valor 4x
    n = int(input('Digite um número: '))
    s += n #ou s = s + n 
print (f'O somatório de todos os valores foi {s}.')

print ('-' * 20)