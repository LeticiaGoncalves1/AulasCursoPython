# Importa a função factorial do módulo math
from math import factorial

# Solicita que o usuário digite um número inteiro
n = int(input('Digite um número para calcular seu Fatorial: '))

# Calcula o fatorial do número fornecido usando a função factorial
f = factorial(n)

# Imprime o resultado do cálculo
print(f'O fatorial de {n} é {f}.')

#-----------------------------------------------------------
# ou podemos fazer dessa forma

# Solicita que o usuário digite um número inteiro
n = int(input('Digite um número para calcular seu Fatorial: '))

# Verifica se o número é negativo
if n < 0:
    print('O fatorial não está definido para números negativos.')

# Caso o número seja zero, o fatorial é 1
elif n == 0:
    print ('O fatorial de 0 é 1.')

# Se o número for positivo, calcula o fatorial
else:
    # Inicializa um contador para percorrer os números de n até 1
    contador = n

    # Inicializa uma variável para armazenar o fatorial, começando com 1
    fatorial = 1

# Imprime a parte inicial da expressão, mostrando qual fatorial está sendo calculado
print(f'Calculando {n}! = ', end = '')

# Entra em um loop enquanto o contador for maior que 0
while contador > 0:
    # Imprime o valor atual do contador
    print(f'{contador}', end = '')

    # Imprime ' x ' se o contador for maior que 1, caso contrário, imprime ' = '
    print(' x ' if contador > 1 else ' = ', end = '')

    # Calcula o fatorial multiplicando-o pelo valor atual do contador
    fatorial = fatorial * contador

    # Decrementa o contador
    contador = contador - 1

# Imprime o resultado do fatorial calculado
print(f'{fatorial}')
print ('')
# -------------------------------------------------------
# Em for

# Solicita ao usuário um número para calcular o fatorial e converte a entrada para um número inteiro.
n = int(input('Digite um número para calcular seu Fatorial: '))

# Inicializa duas variáveis: contador para rastrear o número atual e fatorial para armazenar o resultado.
contador = n
fatorial = 1

# Imprime a mensagem inicial para mostrar qual fatorial está sendo calculado.
print(f'Calculando {n}! = ', end='')

# Inicia um loop for que conta de n até 1 (inclusive), decrementando 1 em cada iteração.
for n in range(n, 0, -1):
    # Imprime o valor atual do contador.
    print(f'{contador}', end='')

    # Imprime ' x ' se o contador atual for maior que 1, caso contrário, imprime ' = ' para indicar o final da expressão.
    print(' x ' if contador > 1 else ' = ', end='')

    # Calcula o fatorial multiplicando o valor atual do fatorial pelo valor atual do contador.
    fatorial = fatorial * contador

    # Decrementa o contador em 1 para a próxima iteração.
    contador = contador - 1

# Imprime o resultado do fatorial.
print(f'{fatorial}')
print('')
