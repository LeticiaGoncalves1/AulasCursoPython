from time import sleep
print ('---' * 20)
print ('{:^60}'.format(' Loja Pythícia ')) #Esse código alinha a frase no meio dos espaços.
print ('---' * 20)
preco = float(input('Digite o valor da sua compra: R$'))

print ('PROCESSANDO PAGAMENTO...')
sleep(2)
print ('---' * 20)

print ('''               💰💰FORMAS DE PAGAMENTO💰💰

[ 1 ] À VISTA - DINHEIRO💵/CHEQUE🧾: 10% DE DESCONTO.
[ 2 ] À VISTA - CARTÃO💳: 5% DE DESCONTO
[ 3 ] EM ATÉ 2X NO CARTÃO💳: PREÇO NORMAL.
[ 4 ] EM 3X OU MAIS NO CARTÃO💳: 20% DE JUROS.''')

print ('---' * 20)

escolha = int(input('Qual a opção desejada? '))

print ('---' * 20)

if escolha == (1):
    total = preco - (preco * 10 / 100)
    print (f'O valor da sua compra com desconto,foi de R${total:.2f}, obrigada pela preferência!')

elif escolha == (2):
    total = preco - (preco * 5 / 100)
    print (f'O valor da sua compra com desconto, foi de R${total:.2f}, obrigada pela preferência!')

elif escolha == (3):
    total = preco
    parcela = preco / 2;
    print (f'A sua compra foi parcelada em 2x de R${parcela:.2f} sem JUROS, tendo um total de R${total:.2f}, obrigada pela preferência!')
    
elif escolha == (4):
    total = preco + (preco * 20 / 100)
    totparc = int(input('Em quantas vezes deseja parcelar?'))
    parcela = total / totparc
    print (f'A sua compra será parcelada em {totparc}x de R${parcela:.2f}, com JUROS, o valor de sua compra foi de {preco:.2f}, e ficou no total de R${total:.2f}, obrigada pela preferência!')

print ('FIM')