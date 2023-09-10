n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

média = (n1 + n2) / 2
print (f'Sua média foi {média:.1f}')

if média < 5:
    print('REPROVADO!')
elif média >= 5 and média <= 6.9:
    print ('RECUPERAÇÃO!')
elif média >= 7:
    print ('APROVADO!')