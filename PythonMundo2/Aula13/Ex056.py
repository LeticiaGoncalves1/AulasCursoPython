somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for i in range (1, 5):
    print (f'----- {i} PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade

    if i == 1 and sexo in 'Mm': #M maiúsculo e minúsculo para verificar ambos
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print ('')
mediaidade = somaidade / 4
print (f'A média da idade dos participantes da pesquisa é {mediaidade:.2f} anos.')
print (f'O homem mais velho tem {maioridadehomem}, e o nome dele é {nomevelho}.')
print (f'Ao todo, são {totmulher20} mulheres menores de 20 anos.')
print ('')