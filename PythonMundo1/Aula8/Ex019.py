import random
a1 = str(input('Primeiro Aluno:'))
a2 = str(input('Segundo Aluno:'))
a3 = str(input('Terceiro Aluno:'))
a4 = str(input('Quarto Aluno:'))
lista = []
lista.append(a1)
lista.append(a2)
lista.append(a3)
lista.append(a4)
escolhido = random.choice(lista)
print (f'O aluno escolhido foi {escolhido}')