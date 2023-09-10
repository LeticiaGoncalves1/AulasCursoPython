print ('início')
nota = 0 
soma = 0
contador = 0
while True:
    #nome = str(input('Nome do aluno:'))
    nota = float(input('Digite a nota:'))
    soma = soma + nota
    contador = contador + 1
    print (contador)
    fim = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
    if fim == 'S':
        continue
    elif fim == 'N':
        break
print (F'Soma {soma:.1f}, quantas notas foram anotadas: {contador}')
media = soma / contador
print (f'Sua média foi {media:.1f}')
print ('Fim do programa.')
