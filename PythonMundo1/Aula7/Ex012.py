p = float(input('Digite o preço do produto desejado: '))    #PreçoInicial
d = p * 5 / 100      #desconto5%
pd = p - d #PreçoComDesconto
print ('-' * 40)
print ('                 Descontos')
print ('-' * 40)
print (f'o preço do produto desejado inicialmente era de R${p:.2f}')
print (f'com 5% de desconto, ele terá um desconto de R${d:.2f} e sairá por R${pd:.2f}')