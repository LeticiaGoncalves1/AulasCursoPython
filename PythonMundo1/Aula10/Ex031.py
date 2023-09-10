d = float(input('Digite a distância da viagem:'))
print (f'Você está prestes a fazer uma viagem de {d}Km de distância.')
if d <= 200:
    passagem = d * 0.50
    print (f'Sua passagem ficou no valor de R${passagem:.2f}')
else:
    passagem = d * 0.45
    print (f'Sua passagem ficou no valor de R${passagem:.2f}')