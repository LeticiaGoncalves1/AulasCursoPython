s = float(input('Digite o seu salário atual: '))    #SalárioAtual
a = s * 15 / 100    #Aumento15%
ns = s + a    #NovoSalário
print ('-' * 40)
print ('                NOVO SALÁRIO')
print ('-' * 40)
print (f'Seu salário inicial era de R${s:.2f}')
print (f'Você teve um aumento de 15% nele, equivalente à R${a:.2f}')
print (f'Seu novo salário será de R${ns:.2f}. PARABÉNS!!!')