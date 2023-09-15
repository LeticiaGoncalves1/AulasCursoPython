print ('--- Verificador de palíndromo ---')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separando as palavras da frase
junto = ''.join(palavras) #juntando a frase, agora sem os espaços internos.
inverso = junto[::-1]

#inverso = ''
#começa antes da primeira letra, vai até depois da ultima letra, e mostra de trás para frente. ↓
#for letra in range (len(junto) -1, -1, -1):
#    inverso += junto[letra] #modo de fazer com for
   
print (f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print ('Temos um palíndromo!')

else:
    print ('A frase digitada não é um palíndromo!')

