print ('--' * 30)
print ('        CALCULO DE ÍNDICE DE MASSA CORPÓREA!    ')
print ('--' * 30)
peso = float(input('Digite o seu peso(Kg)'))
altura = float(input('Digite a sua altura:(m)'))
print (f'--' * 30)
imc = peso / (altura ** 2) # ou peso / (altura * altura)
print (f'Eu índice de massa corporal é {imc:.1f}')

if imc < 18.5:
    print ('Abaixo do peso, CUIDADO!')
elif imc >= 18.5 and imc <= 25:
    print ('Peso ideal')
elif imc > 25.1 and imc <= 30:
    print ('Sobrepeso')
elif imc > 30.1 and imc <= 40:
    print ('Obesidade')
elif imc > 40:
    print ('Obesidade mórbida. CUIDADO!')
