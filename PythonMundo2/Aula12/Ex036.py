print ('---' * 16)
print ('EMPRÉSTIMO BANCARIO PARA FINANCIAMENTO DE IMÓVEIS   ')
print ('---' * 16)


casa = float(input('Qual é o valor do imóvel que deseja financiar? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar o imóvel? '))

print ('-' * 40)

salário30 = salário * 30 / 100
numparcelas = anos * 12
parcela = casa / numparcelas

if parcela < salário30:
    print (f'Parabéns, seu financiamento foi aprovado!')
    print (f'O número de parcelas do seu financiamento é de {numparcelas}x')
    print (f'O valor das suas parcelas é R${parcela:.2f}')
elif parcela > salário30:
    print ('Financiamento negado!')
    print (f'30% do seu salário é R${salário30:.2f}')
    print (f'O número de parcelas vai ser {numparcelas}')
    print (f'O valor das suas parcelas será {parcela:.2f}')
