salário = float(input('Qual seu salário atual? R$'))

if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
if salário >= 1250:
    aumento = salário + (salário * 10 / 100)

print (f'seu salário anterior era R${salário}, e seu novo salário é R${aumento}')