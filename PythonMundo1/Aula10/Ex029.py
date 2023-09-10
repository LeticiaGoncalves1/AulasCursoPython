velo = float(input('Qual velocidade atual do seu carro está:'))
if velo > 80: #Condição Simples!
    print ('MULTADO!!!')
    print ('Você excedeu o milite permitido, que é 80Km/h')
    multa = (velo-80) * 7
    print (f'O valor da sula multa é R${multa:.2f}')
print ('Tenha um bom dia! Dirija com segurança!')