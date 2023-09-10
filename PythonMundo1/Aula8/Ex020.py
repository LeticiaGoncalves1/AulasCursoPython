import random
lista = []
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista.append (n1)
lista.append (n2)
lista.append (n3)
lista.append (n4)
random.shuffle(lista)
print ('A ordem de apresentação dos alunos é')
print (lista)