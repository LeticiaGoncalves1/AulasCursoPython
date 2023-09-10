n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

menor = int
maior = int

menor = n1
maior = n2

if n3 < menor:
    menor = n3
if n2 < menor:
    menor = n2
if n1 < menor:
    menor = n1

if n3 > maior:
    maior = n3
if n2 > maior:
    maior = n2
if n1 > maior:
    maior = n1

print (f'O menor número é {menor}')
print (f'O maior número é {maior}')