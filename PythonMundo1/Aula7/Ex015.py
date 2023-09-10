dias = int(input('Você alugou o carro por quantos dias?'))
km = float(input('Quantos km você percorreu?'))
pago = (dias * 60) + (km * 0.15)
print (f'O total a pagar é R${pago:.2f}')